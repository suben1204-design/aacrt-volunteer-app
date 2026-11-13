# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「四語題庫精準路由、跑馬燈外語隔離與第 15～17 題現場服務擴充」（`aacrt-guide-v2.19`）：
1. **問答路由順序與攔截修復（`generateLocalBrainAnswerBundle`）**：
   - 修復第 1 題（Keynote）過度排除，並將第 14 題（三日總日程＋開閉幕／頒獎關鍵字）移至第 2 題前。
   - 將第 2 題（7F 會議室／地圖）移至第 17 題之後，徹底解決 `luggage room`、`first aid room`、`会場に荷物預かり` 被提前攔截的 Bug。
   - 補齊第 5、6、8 題（午餐／晚宴／禁菸與電子煙）日韓自然口語同義詞，並強化第 0 題無資料論文編號四語兜底。
   - 新增第 15～17 題四語現場服務題庫（行李寄放、茶歇飲水充電、醫護與遺失物協尋）。
2. **UI 與跑馬燈外語隔離（`index.html` + `sw.js`）**：
   - `#ticker-text` 跑馬燈隔離後台中文內容，非 `zh-TW` 模式一律顯示對應母語公告。
   - 補齊地圖燈箱標籤與雙擊放大提示、文件標籤（`高清圖檔`/`PDF 手冊`）、頁尾版本前綴與 `.sim-time-btn` 時段按鈕之四語切換。
   - PWA 快取推進為 `aacrt-guide-v2.19`。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（待本次 commit + push 至 `main` 更新為 `v2.19`）。
- **GAS 後端程式碼**：`gas/Code.js`（已含 `gemini-2.5-flash` 與 `CacheService` 60 秒快取，**待貼回 Google Apps Script 發佈新版本**）。
- **論文測試基準庫**：`docs/abstracts_index.json`（第 59 次年會 217 篇測試資料；口頭 74 篇、海報 143 篇）。

## ➡️ 下一步可做事項
1. **更新 GAS 線上部署**：將 `gas/Code.js` 最新內容貼回 Google Apps Script，重新發佈新版本部署，並確認指令碼屬性已設定 `GEMINI_API_KEY`。
2. **實機手機 PWA 測試**：測試四語切換（含跑馬燈、地圖燈箱、時段按鈕）、第 1/14/15/16/17 題問答精準度與雲端 Gemini 2.5 Flash 自由提問。
3. **正式 2027 AACRT 資料置換**：待正式 Excel 定稿後放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。

## 🕐 最後更新
- 時間：2026-11-13 13:32
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
