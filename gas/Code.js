/**
 * 2027 AACRT 智慧大腦問答監控後端 (Google Apps Script)
 * 專案名稱：2027 AACRT 現場問答監控儀表板
 * 功能：
 * 1. 接收前端 Web App 提問紀錄 (POST)，寫入 Google 試算表（非同步、零卡頓）。
 * 2. 即時緊急跑馬燈同步 (GET)，回傳首列緊急廣播文字與當前狀態。
 * 3. 特殊求助關鍵字監控 (Special Assistance Alert)，自動發信或推播給大會幹部。
 * 4. 2027/04/26 12:00 自動落日關閉防護 (Sunset Guardrail)。
 */

// 試算表設定（若綁定試算表，預設開啟當前試算表；亦可指定 SPREADSHEET_ID）
var SPREADSHEET_ID = ""; // 若未填寫則自動取得主動試算表，或以第一張工作表為準
var SHEET_LOGS = "即時提問紀錄";
var SHEET_CONFIG = "大會設定與跑馬燈";

// 幹部通報 Email（預設為大會負責人）
var LEADER_EMAIL = "suben1204@gmail.com";

// 落日時間點：2027-04-26 12:00:00 (台北時間 GMT+8)
var SUNSET_TIMESTAMP = new Date("2027-04-26T12:00:00+08:00").getTime();

/**
 * 處理 GET 請求：前端抓取最新緊急跑馬燈與大會設定
 */
function doGet(e) {
  try {
    var now = new Date().getTime();
    if (now >= SUNSET_TIMESTAMP) {
      return jsonResponse({
        status: "sunset",
        message: "2027 AACRT 已圓滿閉幕，感謝您的參與！",
        ticker: "2027 AACRT 亞澳區醫事放射學術年會已圓滿閉幕，感謝全體貴賓與志工夥伴！",
        allow_query: false
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

    return jsonResponse({
      status: "active",
      ticker: ticker,
      version: version,
      allow_query: true,
      server_time: new Date().toISOString()
    });
  } catch (err) {
    return jsonResponse({
      status: "error",
      message: err.toString(),
      ticker: "大會現場公告：歡迎蒞臨 2027 AACRT 國際學術年會！",
      allow_query: true
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
    var source = payload.source || "web_pwa"; // web_pwa 或 volunteer_badge
    var needHelp = payload.need_help || false;

    // 特殊求助關鍵字自動偵測（醫療急救、外國人走失、外國學者投訴、貴重物品丟失）
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

    // 若判定為特殊急迫求助，立刻觸發 Email / Webhook 通知幹部
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
 * 幹部推播警報（MailApp 備用推播，零成本、即時到達）
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
 * 試算表初始化函式（首次部署或手動執行，自動建構漂亮儀表板結構）
 */
function initConferenceSpreadsheet() {
  var ss = getSpreadsheet();
  
  // 1. 初始化設定頁
  var configSheet = ss.getSheetByName(SHEET_CONFIG);
  if (!configSheet) {
    configSheet = ss.insertSheet(SHEET_CONFIG);
  }
  configSheet.clear();
  configSheet.getRange("A1:B3").setValues([
    ["即時跑馬燈公告 (改此格即全場同步)", "大會現場公告：7 樓大會堂開幕式預計於 09:00 正式開始，歡迎提早入場。"],
    ["知識庫版本號 (Version)", "2027.04.24-v1.5"],
    ["落日關閉時間 (Sunset Time)", "2027-04-26 12:00:00 (GMT+8)"]
  ]);
  configSheet.getRange("A1:A3").setBackground("#1e293b").setFontColor("#fbbf24").setFontWeight("bold");
  configSheet.setColumnWidth(1, 260);
  configSheet.setColumnWidth(2, 600);

  // 2. 初始化日誌頁
  var logSheet = ss.getSheetByName(SHEET_LOGS);
  if (!logSheet) {
    logSheet = ss.insertSheet(SHEET_LOGS);
  }
  logSheet.clear();
  logSheet.appendRow(["提問時間 (台北時間)", "來源端", "發問語言", "提問內容 (User Query)", "大腦/AI回覆摘要", "特殊求助警示", "處理狀態"]);
  logSheet.getRange(1, 1, 1, 7).setBackground("#0f172a").setFontColor("#fbbf24").setFontWeight("bold");
  logSheet.setColumnWidth(1, 160);
  logSheet.setColumnWidth(2, 100);
  logSheet.setColumnWidth(3, 90);
  logSheet.setColumnWidth(4, 300);
  logSheet.setColumnWidth(5, 300);
  logSheet.setColumnWidth(6, 120);
  logSheet.setColumnWidth(7, 120);

  Logger.log("2027 AACRT 試算表儀表板初始化完成！");
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
