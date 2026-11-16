# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「頂部公告列跑馬燈化與移除右上角 Taiwan 時鐘」（`aacrt-guide-v2.20`）：
1. **移除右上角 Taiwan 時鐘**：移除 `#taiwan-clock` 與 `updateClock()`，將頂部 `LIVE` 公告列完整寬度讓給公告內容（不影響「我的行程」頁籤之台北時間判定邏輯）。
2. **改為左右滾動跑馬燈**：為 `#ticker-text` 加入純 CSS `.animate-ticker`（16 秒循環左移，滑鼠移入或手指按住自動暫停），解決手機端長公告被截斷問題。
3. **PWA 快取推進**：`sw.js` 推進為 `aacrt-guide-v2.20`。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（待本次 commit + push 至 `main` 更新為 `v2.20`）。
- **GAS 後端程式碼**：`gas/Code.js`（已含 `gemini-2.5-flash` 與 `CacheService` 60 秒快取，**待貼回 Google Apps Script 發佈新版本**）。
- **論文測試基準庫**：`docs/abstracts_index.json`（第 59 次年會 217 篇測試資料；口頭 74 篇、海報 143 篇）。

## ➡️ 下一步可做事項
1. **更新 GAS 線上部署**：將 `gas/Code.js` 最新內容貼回 Google Apps Script，重新發佈新版本部署，並確認指令碼屬性已設定 `GEMINI_API_KEY`。
2. **實機手機 PWA 測試**：確認頂部 `LIVE` 跑馬燈在手機上的滾動速度與閱讀體驗，以及四語切換與問答功能。
3. **正式 2027 AACRT 資料置換**：待正式 Excel 定稿後放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。

## 🕐 最後更新
- 時間：2026-11-16 08:15
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
