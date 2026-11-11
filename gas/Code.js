/**
 * 2027 AACRT 智慧大腦問答監控後端 (Google Apps Script)
 * 專案名稱：2027 AACRT 現場問答監控儀表板
 * 功能：
 * 1. 接收前端 Web App 提問紀錄 (POST)，寫入 Google 試算表（非同步、零卡頓）。
 * 2. 即時動態統計「熱門提問 TOP 榜單」，供前端即時動態抓取展示 (GET)。
 * 3. 即時緊急跑馬燈同步 (GET)，回傳首列緊急廣播文字與當前狀態。
 * 4. 特殊求助關鍵字監控 (Special Assistance Alert)，自動發信或推播給大會幹部。
 * 5. 2027/04/26 12:00 自動落日關閉防護 (Sunset Guardrail)。
 */

var SPREADSHEET_ID = ""; // 若未填寫則自動取得主動試算表，或以第一張工作表為準
var SHEET_LOGS = "即時提問紀錄";
var SHEET_CONFIG = "大會設定與跑馬燈";

// 幹部通報 Email
var LEADER_EMAIL = "suben1204@gmail.com";

// 落日時間點：2027-04-26 12:00:00 (台北時間 GMT+8)
var SUNSET_TIMESTAMP = new Date("2027-04-26T12:00:00+08:00").getTime();

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
    var configSheet = ss.getSheetByName(SHEET_CONFIG);
    var ticker = "大會現場公告：7 樓大會堂開幕式預計於 09:00 正式開始，歡迎提早入場。";
    var version = "v1.5";

    if (configSheet) {
      var tickerCell = configSheet.getRange("B1").getValue();
      if (tickerCell) ticker = tickerCell.toString();
      var versionCell = configSheet.getRange("B2").getValue();
      if (versionCell) version = versionCell.toString();
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
 * 處理 POST 請求：前端送來提問、語言、回覆摘要與特殊求助
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
      payload = JSON.parse(e.postData.contents);
    } else if (e.parameter) {
      payload = e.parameter;
    }

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

    // 寫入 Google 試算表
    var ss = getSpreadsheet();
    var logSheet = ss.getSheetByName(SHEET_LOGS);
    if (!logSheet) {
      logSheet = ss.insertSheet(SHEET_LOGS);
      logSheet.appendRow(["提問時間 (台北時間)", "來源端", "發問語言", "提問內容 (User Query)", "大腦/AI回覆摘要", "特殊求助警示", "處理狀態"]);
      logSheet.getRange(1, 1, 1, 7).setBackground("#0f172a").setFontColor("#fbbf24").setFontWeight("bold");
    }

    var timeStr = Utilities.formatDate(new Date(), "Asia/Taipei", "yyyy-MM-dd HH:mm:ss");
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
    return SpreadsheetApp.openById(SPREADSHEET_ID);
  }
  return SpreadsheetApp.getActiveSpreadsheet() || SpreadsheetApp.create("2027 AACRT 現場問答監控儀表板");
}

/**
 * 輔助工具：標準 JSON 回應包裝
 */
function jsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
