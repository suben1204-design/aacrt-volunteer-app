# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
已全面完成專案路線圖的**階段五（Google Apps Script 雲端中繼儀表板）**與**階段六（GitHub Pages 正式上線公開發布）**：
1. **GitHub Pages 正式發布生效**：
   - 線上正式網址：`https://suben1204-design.github.io/aacrt-volunteer-app/`（HTTP 200 OK，全球 CDN 快取分發）。
   - GitHub 儲存庫：`suben1204-design/aacrt-volunteer-app`。
2. **Google Apps Script 雲端中繼部署完成（Web App）**：
   - 專案名稱：`2027 AACRT 現場問答監控儀表板`
   - 部署 ID：`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`
   - 端點網址：`https://script.google.com/macros/s/AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw/exec`
   - 功能實測：
     - **非同步日誌寫入**：前端發問即時以 `mode: 'no-cors'` 送出，0 延遲零卡頓，寫入試算表「即時提問紀錄」。
     - **即時跑馬燈公告同步**：幹部於試算表 `B1` 改字，前端即時同步大會緊急通告。
     - **緊急特殊求助警報**：自動過濾急救、胸痛、呼吸困難、走失、護照遺失等關鍵字，自動推播發信至 `suben1204@gmail.com`。
     - **落日安全防護**：2027-04-26 12:00 起後端拒收新問題，前端切換感謝紀念卡，維護 0 額外費用。
3. **前端（`index.html`）全面串接生效**：
   - 成功將 `GAS_ENDPOINT_URL` 植入前端，並加入 `fetchLiveTicker()` 與 `syncLogToBackend()`。

## 🚦 目前狀態
- **專案已 100% 交付完成（階段一至階段六全線打通）**。
- 任何人拿起手機掃描名牌 QR Code 即可連入線上版 PWA 體驗四語問答、語音朗讀與離線手冊。

## ➡️ 後續維護指引
- **大會資料更新**：隨時將大會官方手冊或議程丢入 `創作庫-內部原創層/`，執行 `python scripts/compile_brain.py` 即可自動歸檔舊檔並升級大腦。
- **預算防護設定**：可參考專案建議於 Google Cloud 設置 $50 美元（NT$ 1,600）硬性配額上限防護牆。

## 🕐 最後更新
- 時間：2026-11-11 23:22
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
