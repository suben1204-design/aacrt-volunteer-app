# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「全系統健檢與雲端 AI／高併發修復」（`aacrt-guide-v2.17`）：
1. **雲端 Gemini AI 串接修復（`index.html` + `gas/Code.js`）**：
   - 修復 `fetchCloudBrainAnswer()` 原檢查 `data.success` 與 GAS 回傳 `data.status === 'success'` 不符導致雲端 AI 回覆永遠降級的 Bug。
   - 調整超時保護從 5 秒放寬至 10 秒（`10000ms`），並於 `sendMessage()`／`deliverAiResponse()` 加入 `skipLogSync` 避免 `ask_ai` 重複寫入兩筆試算表紀錄。
   - `gas/Code.js` 將模型從已下線的 `gemini-1.5-flash` 升級為 **`gemini-2.5-flash`**，並加上 Markdown code fence 清理與四語保底。
2. **GAS 高併發 60 秒快取優化（`gas/Code.js`）**：
   - `doGet()` 加入 `CacheService.getScriptCache()` 60 秒快取（`AACRT_GET_CACHE_V1`），降低多人同時掃描 QR Code 進站時對 Google Sheets 的讀寫壓力。
3. **PWA 快取推進**：`sw.js` 推進為 `aacrt-guide-v2.17`。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（待推上 `main` 更新為 `v2.17`）。
- **GAS 後端程式碼**：已更新本地 `gas/Code.js`，**尚未重新貼回 Google Apps Script 並發佈新版本**。
- **論文測試基準庫**：`docs/abstracts_index.json`（第 59 次年會 217 篇測試資料；口頭 74 篇、海報 143 篇）。
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`

## ➡️ 下一步可做事項
1. **更新 GAS 線上部署**：將 `gas/Code.js` 最新內容貼回 Google Apps Script，重新發佈新版本部署，並確認指令碼屬性已設定 `GEMINI_API_KEY`。
2. **實機手機 PWA 測試**：測試本地 14 題、論文編號免括號查詢、以及第 2 層雲端 Gemini 2.5 Flash 自由提問。
3. **正式 2027 AACRT 資料置換**：待正式 Excel 定稿後放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。
- GAS 免費版同時執行上限約 30 併發；透過 `CacheService` 可舒緩 `doGet` 讀表壓力，但若開幕瞬間高併發寫入仍有排隊可能（前端已具備自動降級機制）。

## 🕐 最後更新
- 時間：2026-11-13 13:20
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
