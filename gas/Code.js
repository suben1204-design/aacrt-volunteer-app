/**
 * 2027 AACRT 智慧大腦問答監控後端 (Google Apps Script)
 * 專案名稱：2027 AACRT 現場問答監控儀表板
 * 功能：
 * 1. 接收前端 Web App 提問紀錄 (POST)，寫入 Google 試算表（非同步、零卡頓）。
 * 2. 即時動態統計「熱門提問 TOP 榜單」，供前端即時動態抓取展示 (GET)。
 * 3. 即時緊急跑馬燈同步 (GET)，回傳首列緊急廣播文字與當前狀態。
 * 4. 特殊求助關鍵字監控 (Special Assistance Alert)，自動發信或推播給大會幹部。
 * 5. 雲端智慧大腦混合架構 (Gemini Flash / 外交禮賓導流)。
 * 6. 2027/04/26 12:00 自動落日關閉防護 (Sunset Guardrail)。
 */

// 綁定正式 Google 試算表 ID
var SPREADSHEET_ID = "1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc";
var SHEET_LOGS = "即時提問紀錄";
var SHEET_CONFIG = "大會設定與跑馬燈";

// 幹部通報 Email
var LEADER_EMAIL = "suben1204@gmail.com";

// 落日時間點：2027-04-26 12:00:00 (台北時間 GMT+8)
var SUNSET_TIMESTAMP = new Date("2027-04-26T12:00:00+08:00").getTime();

/**
 * 確保試算表具備工作表與初始設定
 */
function ensureSheetsConfigured(ss) {
  var configSheet = ss.getSheetByName(SHEET_CONFIG);
  if (!configSheet) {
    var sheets = ss.getSheets();
    if (sheets.length === 1 && sheets[0].getLastRow() === 0) {
      configSheet = sheets[0];
      configSheet.setName(SHEET_CONFIG);
    } else {
      configSheet = ss.insertSheet(SHEET_CONFIG);
    }
    configSheet.getRange("A1").setValue("即時跑馬燈公告 (可隨時修改 B1)");
    configSheet.getRange("B1").setValue("大會現場公告：7 樓大會堂開幕式預計於 09:00 正式開始，歡迎提早入場。");
    configSheet.getRange("A2").setValue("大腦版本");
    configSheet.getRange("B2").setValue("v1.06");
    configSheet.getRange("A3").setValue("操作指南");
    configSheet.getRange("B3").setValue("大會幹部直接在此處修改 B1，所有與會學者及志工手機 APP 即刻於重整或 60 秒內即時更新！");
    
    configSheet.getRange("A1:A3").setBackground("#0f172a").setFontColor("#fbbf24").setFontWeight("bold");
    configSheet.getRange("B1").setFontColor("#1e3a8a").setFontWeight("bold").setFontSize(11);
    configSheet.setColumnWidth(1, 260);
    configSheet.setColumnWidth(2, 650);
  }

  var logSheet = ss.getSheetByName(SHEET_LOGS);
  if (!logSheet) {
    logSheet = ss.insertSheet(SHEET_LOGS);
    logSheet.appendRow(["提問時間 (台北時間)", "來源端", "發問語言", "提問內容 (User Query)", "大腦/AI回覆摘要", "特殊求助警示", "處理狀態"]);
    logSheet.getRange(1, 1, 1, 7).setBackground("#0f172a").setFontColor("#fbbf24").setFontWeight("bold");
    logSheet.setColumnWidth(1, 170);
    logSheet.setColumnWidth(4, 250);
    logSheet.setColumnWidth(5, 300);
  }
  return { configSheet: configSheet, logSheet: logSheet };
}

/**
 * 手動初始化專用函數（可直接在 Apps Script 編輯器執行）
 */
function initSpreadsheet() {
  var ss = getSpreadsheet();
  ensureSheetsConfigured(ss);
  Logger.log("試算表初始化完成！");
}

/**
 * 處理 GET 請求：前端抓取最新緊急跑馬燈、大會設定以及「即時熱門提問排行榜」
 */
function doGet(e) {
  try {
    var now = new Date().getTime();
    if (now >= SUNSET_TIMESTAMP) {
      return jsonResponse({
        status: "sunset",
        message: "2027 AACRT 已圓滿閉幕，感謝您的參與！",
        ticker: "2027 AACRT 亞澳區醫事放射學術年會已圓滿閉幕，感謝全體貴賓與志工夥伴！",
        allow_query: false,
        top_queries: []
      });
    }

    var ss = getSpreadsheet();
    var sheetsObj = ensureSheetsConfigured(ss);
    var configSheet = sheetsObj.configSheet;
    
    var ticker = "大會現場公告：7 樓大會堂開幕式預計於 09:00 正式開始，歡迎提早入場。";
    var version = "v1.06";

    if (configSheet) {
      var tickerCell = configSheet.getRange("B1").getValue();
      if (tickerCell && tickerCell.toString().trim() !== "") {
        ticker = tickerCell.toString().trim();
      }
      var versionCell = configSheet.getRange("B2").getValue();
      if (versionCell && versionCell.toString().trim() !== "") {
        version = versionCell.toString().trim();
      }
      // 若原試算表仍保留舊版 v1.04/v1.05，自動幫主管升級為 v1.06
      if (version === "v1.04" || version === "v1.05") {
        version = "v1.06";
        configSheet.getRange("B2").setValue("v1.06");
      }
    }

    // 動態統計試算表日誌中「最常被問的 TOP 問題」
    var topQueries = getTopFrequentQueries(ss);

    return jsonResponse({
      status: "active",
      ticker: ticker,
      version: version,
      allow_query: true,
      top_queries: topQueries,
      server_time: new Date().toISOString()
    });
  } catch (err) {
    return jsonResponse({
      status: "error",
      message: err.toString(),
      ticker: "大會現場公告：歡迎蒞臨 2027 AACRT 國際學術年會！",
      allow_query: true,
      top_queries: []
    });
  }
}

/**
 * 處理 POST 請求：前端送來提問、語言、回覆摘要與特殊求助，或請求雲端 AI 問答
 */
function doPost(e) {
  try {
    var now = new Date().getTime();
    if (now >= SUNSET_TIMESTAMP) {
      return jsonResponse({
        status: "sunset",
        message: "大會已閉幕，停止接收新提問。"
      });
    }

    var payload = {};
    if (e.postData && e.postData.contents) {
      try {
        payload = JSON.parse(e.postData.contents);
      } catch (pe) {
        payload = { query: e.postData.contents };
      }
    } else if (e.parameter) {
      payload = e.parameter;
    }

    var action = payload.action || "";
    var query = payload.query || "";
    var reply = payload.reply || "";
    var lang = payload.lang || "zh-TW";
    var source = payload.source || "web_pwa";
    var needHelp = payload.need_help || false;

    // 特殊求助關鍵字自動偵測
    var alertKeywords = ["胸痛", "呼吸困難", "昏倒", "急救", "走失", "護照遺失", "偷竊", "緊急", "anaphylaxis", "heart attack", "lost passport", "emergency", "救急", "パスポート紛失"];
    var isEmergency = needHelp;
    if (!isEmergency) {
      for (var i = 0; i < alertKeywords.length; i++) {
        if (query.toLowerCase().indexOf(alertKeywords[i].toLowerCase()) !== -1) {
          isEmergency = true;
          break;
        }
      }
    }

    var ss = getSpreadsheet();
    var sheetsObj = ensureSheetsConfigured(ss);
    var logSheet = sheetsObj.logSheet;
    var timeStr = Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss");

    // 模式一：雲端智慧大腦動態問答 (action: 'ask_ai')
    if (action === 'ask_ai') {
      var aiBundle = handleCloudAiQuery(query, lang);
      var alertBadge = isEmergency ? "🚨 特殊急迫求助" : "雲端AI諮詢";
      var status = isEmergency ? "待幹部跟進" : "雲端解答/外交導流";
      var replySummary = (aiBundle["zh-TW"] || "").substring(0, 150);

      logSheet.appendRow([timeStr, source, lang, query, replySummary, alertBadge, status]);

      if (isEmergency) {
        notifyLeader(timeStr, lang, query, replySummary);
      }

      return jsonResponse({
        status: "success",
        matched: false,
        bundle: aiBundle
      });
    }

    // 模式二：一般前台日誌同步
    var alertBadge = isEmergency ? "🚨 特殊急迫求助" : "一般諮詢";
    var status = isEmergency ? "待幹部跟進" : "系統自動解答";

    logSheet.appendRow([timeStr, source, lang, query, reply.substring(0, 150), alertBadge, status]);

    // 特殊急迫求助觸發郵件通知
    if (isEmergency) {
      notifyLeader(timeStr, lang, query, reply);
    }

    return jsonResponse({
      status: "success",
      recorded_at: timeStr,
      is_emergency: isEmergency
    });

  } catch (err) {
    return jsonResponse({
      status: "error",
      message: err.toString()
    });
  }
}

/**
 * 處理雲端智慧大腦問答 (若有設定 GEMINI_API_KEY 則呼叫，否則提供四語外交導流)
 */
function handleCloudAiQuery(query, lang) {
  var apiKey = PropertiesService.getScriptProperties().getProperty("GEMINI_API_KEY");
  if (apiKey && apiKey.trim() !== "") {
    try {
      var prompt = "You are the official AI concierge for the 2027 AACRT (Asia-Australasia Conference of Radiographers and Radiological Technologists) & TWSRT 60th Annual Meeting at Taipei Nangang Exhibition Center Hall 2 (TaiNEX 2).\n" +
        "Answer the attendee query clearly, diplomatically, and concisely. Output a strict JSON object with four keys: 'zh-TW', 'en', 'ja', 'ko'.\n" +
        "If the query involves specific locations or procedures you do not know, advise visiting the 1F or 7F Conference Information Desk.\n\n" +
        "Query: " + query;

      var url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + apiKey.trim();
      var reqPayload = {
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: { responseMimeType: "application/json" }
      };

      var options = {
        method: "post",
        contentType: "application/json",
        payload: JSON.stringify(reqPayload),
        muteHttpExceptions: true
      };

      var res = UrlFetchApp.fetch(url, options);
      if (res.getResponseCode() === 200) {
        var resJson = JSON.parse(res.getContentText());
        var rawText = resJson.candidates[0].content.parts[0].text;
        var parsed = JSON.parse(rawText);
        if (parsed["zh-TW"] && parsed["en"]) {
          return parsed;
        }
      }
    } catch (e) {
      Logger.log("Gemini API error: " + e.toString());
    }
  }

  // 預設外交導流四語回覆包
  return {
    "zh-TW": "這項問題涉及大會最新即時安排或特定專屬細節，已為您記錄並同步回報！建議您可直接前往 7 樓或 1 樓「大會官方諮詢服務台」，將由現場幹部為您即時確認處置。",
    "en": "This inquiry involves the latest conference arrangements or specific details, and has been logged! We recommend visiting the Official Information Desk on the 1st or 7th floor for immediate assistance.",
    "ja": "このご質問は大会の最新スケジュールまたは特定の詳細に関するものです。記録いたしましたので、1階または7階の「大会公式インフォメーションデスク」でスタッフにご確認いただくことをお勧めします。",
    "ko": "해당 문의는 대회의 최신 일정 또는 특정 세부 사항과 관련되어 있어 기록되었습니다. 즉각적인 확인을 위해 1층 또는 7층의 '대회 공식 안내 데스크'를 방문해 주시기 바랍니다."
  };
}

/**
 * 幹部推播警報
 */
function notifyLeader(timeStr, lang, query, reply) {
  try {
    var subject = "【🚨 2027 AACRT 現場緊急求助警報】" + query.substring(0, 25);
    var body = "==== 2027 AACRT 智慧大腦現場警報通知 ====\n\n" +
               "【發生時間】： " + timeStr + " (台北時間)\n" +
               "【諮詢語言】： " + lang + "\n" +
               "【提問內容】：\n" + query + "\n\n" +
               "【系統初步引導】：\n" + reply + "\n\n" +
               "----------------------------------------\n" +
               "請現場大會巡場幹部或大會諮詢台志工立刻協助跟進！\n" +
               "（本警報由 2027 AACRT 現場智慧監控後端自動發送）";

    MailApp.sendEmail(LEADER_EMAIL, subject, body);
  } catch (e) {
    Logger.log("Failed to send email alert: " + e.toString());
  }
}

/**
 * 動態統計試算表日誌中「最常被問的問題 TOP 6」
 */
function getTopFrequentQueries(ss) {
  try {
    var logSheet = ss.getSheetByName(SHEET_LOGS);
    if (!logSheet) return [];

    var lastRow = logSheet.getLastRow();
    if (lastRow < 2) return [];

    // 讀取第 4 欄 (D 欄，提問內容)
    var numRows = Math.min(lastRow - 1, 300); // 取最近 300 筆快速統計
    var startRow = Math.max(2, lastRow - numRows + 1);
    var range = logSheet.getRange(startRow, 4, numRows, 1);
    var values = range.getValues();

    var counts = {};
    for (var i = 0; i < values.length; i++) {
      var q = values[i][0];
      if (q && typeof q === 'string') {
        var cleanQ = q.trim();
        if (cleanQ.length > 2) {
          counts[cleanQ] = (counts[cleanQ] || 0) + 1;
        }
      }
    }

    var sorted = Object.keys(counts).sort(function(a, b) {
      return counts[b] - counts[a];
    });

    // 回傳前 6 高頻問題
    return sorted.slice(0, 6);
  } catch (e) {
    Logger.log("Error calculating top queries: " + e.toString());
    return [];
  }
}

/**
 * 輔助工具：取得試算表物件
 */
function getSpreadsheet() {
  if (SPREADSHEET_ID && SPREADSHEET_ID.trim() !== "") {
    return SpreadsheetApp.openById(SPREADSHEET_ID.trim());
  }
  return SpreadsheetApp.getActiveSpreadsheet();
}

/**
 * 輔助工具：標準 JSON 回應包裝
 */
function jsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
