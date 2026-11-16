# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「問答路由順序優化、第 18 題摘要檢索指引與秀給外賓防誤觸」（`aacrt-guide-v2.22`）：
1. **問答路由與題庫擴充（`generateLocalBrainAnswerBundle`）**：
   - 將第 3 題（`ct`/`mri`/`ai`/分廳主題）移至第 14 題（三日總日程）之後，解決 `"Where do I upload my AI slides?"` 與 `"Where is the CT poster area?"` 被提前攔截的衝突。
   - 於第 12 題後新增 **第 18 題（學術論文與摘要檢索指引）** 四語回覆，引導至第一頁「4、學術論文摘要即時檢索」或對話框直接輸入編號查詢。
2. **UX 防誤觸與搜尋擴充（`index.html` + `sw.js`）**：
   - `#show-guest-modal` 內層文字區改為 `max-h-[72dvh] overflow-y-auto` 並加上 `onclick="event.stopPropagation()"`，長文滑動與觸碰不誤關彈窗。
   - `renderOralResults()` 搜尋同步比對發表題目（`title`）與會議室（`room`）；`sendMessage()` 冷卻縮短為 `1500ms` 並提供四語提示。
   - PWA 快取推進為 `aacrt-guide-v2.22`（`sw.js?v=2.22`）。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（待本次 commit + push 至 `main` 更新為 `v2.22`）。
- **GAS 後端部署**：已完成更新至 **10 版**（`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`，含 `gemini-2.5-flash`、`CacheService` 60 秒快取與跑馬燈四語自動翻譯）。
- **論文測試基準庫**：`docs/abstracts_index.json`（第 59 次年會 217 篇測試資料；口頭 74 篇、海報 143 篇）。

## ➡️ 下一步可做事項
1. **實機手機 PWA 測試**：驗證 Google Sheet `B1` 修改中文跑馬燈後四語自動同步、秀給外賓長文滑動、口頭論文題目／會議室關鍵字搜尋與第 18 題檢索指引。
2. **確認 `GEMINI_API_KEY`**：於 GAS 專案「專案設定 → 指令碼屬性」確認已設定 `GEMINI_API_KEY`，以啟用第 2 層雲端自由提問。
3. **正式 2027 AACRT 資料置換**：待正式 Excel 定稿後放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。

## 🕐 最後更新
- 時間：2026-11-16 09:42
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
