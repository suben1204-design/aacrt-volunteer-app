# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「跑馬燈四語自動翻譯同步（GAS 10 版）與題庫／iOS 體驗微調」（`aacrt-guide-v2.21`）：
1. **跑馬燈 Google Sheet 四語自動同步（`gas/Code.js` + `index.html`）**：
   - `gas/Code.js` 於 `doGet()` 讀取 `B1` 後透過 `LanguageApp.translate` 自動翻譯並快取輸出 `ticker_en`、`ticker_ja`、`ticker_ko`（60 秒 `CacheService` 快取 `AACRT_GET_CACHE_V2`），並已完成 GAS 線上部署更新至 **10 版**。
   - 前端 `updateLanguageUI()` 與 `fetchLiveTicker()` 優先顯示對應語系雲端翻譯，若無翻譯則保底顯示最新 `window.cloudTickerText`，不再跳回寫死公告。
2. **題庫精準度與 iOS 體驗微調（`index.html` + `sw.js`）**：
   - 第 9 題補上繁中/日/韓「出席證明 / 參加證明」關鍵字，避免被第 13 題攔截。
   - 第 10 題移除單獨 `access` 並移至第 17 題後、第 2 題前；第 4 題排除充電關鍵字，解決充電站／醫護站／筆電充電誤攔截。
   - `#oral-search-input` 與 `#poster-search-input` 改為 `text-base sm:text-xs` 防 iOS 自動放大，清除鈕加大為 `w-5 h-5`；卡片 1 文案改為「三日」；PWA 快取推進為 `aacrt-guide-v2.21`。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（待本次 commit + push 至 `main` 更新為 `v2.21`）。
- **GAS 後端部署**：已完成更新至 **10 版**（`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`，含 `gemini-2.5-flash`、`CacheService` 60 秒快取與跑馬燈四語自動翻譯）。
- **論文測試基準庫**：`docs/abstracts_index.json`（第 59 次年會 217 篇測試資料；口頭 74 篇、海報 143 篇）。

## ➡️ 下一步可做事項
1. **實機手機 PWA 測試**：驗證 Google Sheet `B1` 修改中文跑馬燈後，切換英／日／韓四語是否皆自動翻譯同步，並測試 iOS 搜尋框防放大與問答路由。
2. **確認 `GEMINI_API_KEY`**：於 GAS 專案「專案設定 → 指令碼屬性」確認已設定 `GEMINI_API_KEY`，以啟用第 2 層雲端自由提問。
3. **正式 2027 AACRT 資料置換**：待正式 Excel 定稿後放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。

## 🕐 最後更新
- 時間：2026-11-16 08:44
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
