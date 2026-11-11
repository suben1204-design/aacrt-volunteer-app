# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成 RDQ 規格交棒與第一版原型核心交付：
1. **多語言大腦資料庫（`aacrt_brain.json`）**：建置完成，收錄交通指引、會議室動線、Wi-Fi、生活實用資訊，支援繁中、英、日、韓四語，並內建未公開問題導流至現場「大會諮詢台」的防禦性規範。
2. **雙用官方 Web App（`index.html`）**：完成手機優先排版、皇家海軍藍×榮耀琥珀金視覺、頂部四語下拉即時切換、60% 快捷手冊分類摺疊卡片、40% 智能對談（含語音輸入 Web Speech API、熱門問題快速問答、自動導引防呆）。
3. **PWA 離線快取機制**：建立 `manifest.json` 與 `sw.js`（Service Worker），南港 2 館網路弱網或無網環境下仍可離線載入核心動線與 FAQ。
4. **Git 與 GitHub**：全部程式碼與資產已成功 Push 至 `suben1204-design/aacrt-volunteer-app`。

## 🚦 目前狀態
- **前端原型與本機大腦已可直接開啟預覽運作（包含四語切換與語音輸入）**。
- 準備進入後端 Google Apps Script 雲端中繼串接（Gemini Flash + Google Sheets 提問記錄）。

## ➡️ 下一步
1. 建立 Google Apps Script 後端中繼程式碼（負責接收提問、呼叫 Gemini Flash、回寫 Google Sheets）。
2. 將前端對話串接至 GAS Web App 端點，完成雲端全自動化。
3. 輸出 $50 美元預算配額設定指南與大會現場 QR Code 產出。

## ⚠️ 注意事項
- 本專案 GitHub repo 為 **PRIVATE（私有）**。
- 本地測試可直接以瀏覽器開啟 `index.html`，語音輸入建議在 Chrome 或 Safari 下點擊麥克風按鈕體驗。

## 🕐 最後更新
- 時間：2026-11-11 21:06
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
