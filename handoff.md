# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「論文檢索雙獨立專區重構、熱門提問精簡防呆、免括號論文查詢、第 14 題三日總日程與四語 UI 補齊」（`aacrt-guide-v2.16`）：
1. **Excel 217 篇測試論文與雙獨立查詢區**：
   - `docs/abstracts_index.json` 含第 59 次年會測試資料共 217 篇（口頭 74 篇、海報 143 篇）。
   - 卡片 4「4、學術論文摘要即時檢索」已改為上下兩大獨立查詢區（`#oral-search-section` 與 `#poster-search-section`），各有獨立搜尋框與「查詢」按鈕：口頭顯示 **論文編號、發表時間、發表題目、會議室、報告者、座長**（6 項）；海報簡潔左右對齊顯示 **論文編號、報告者**（2 項），並已移除卡片上的「問 AI」與「秀給外賓」按鈕。
2. **智慧對談「熱門提問」精簡與單引號/語系修復**：
   - `QUICK_PROMPTS_DATA` 精簡為單排 2 欄（最多 2 個按鈕），`renderDynamicTopQueries()` 改為直接覆蓋前 2 名（不往上堆疊）。
   - 改用 `activeQuickPrompts` + `sendQuickPromptByIndex()`，徹底修復英文單引號（如 `What's`）點擊崩潰 Bug；並隔離非繁中語系（`en`/`ja`/`ko`）不顯示雲端中文熱搜。
3. **本地大腦與四語 UI 全面補齊**：
   - 論文編號查詢放寬為免中括號（`/\[?([OP]-[A-Za-z]{2,5}-\d{1,4})\]?/i`），直接回傳報告者、時間、會議室與座長。
   - 新增 **第 14 題**（三日總日程與每日 08:00/09:00 開放時間）。
   - 補齊 `getFieldLabels()`、`即時線上檢閱`、`#show-guest-modal` 彈窗標籤四語切換，並統一 `shadow-xs`/`shadow-2xs` 為 Tailwind v3 `shadow-sm`。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（HTTP 200 OK，PWA Cache: `aacrt-guide-v2.16`）。
- **論文測試基準庫**：`docs/abstracts_index.json`（217 篇測試資料；2027 AACRT 正式 Excel 尚未上傳，`創作庫-內部原創層/1、論文集/2027 AACRT/` 保持純淨待命）。
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
- **GAS 部署 ID**：`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`（版本 `@9`）

## ➡️ 下一步可做事項
1. **實機手機 PWA 測試**：開啟線上網址測試「口頭／海報」雙獨立查詢區、四國語言切換、免括號論文編號問答與第 14 題三日總日程。
2. **正式 2027 AACRT 資料置換**：待大會定稿 `Excel-口頭--2027 AACRT.xlsx` 與 `Excel-Poster--2027 AACRT.xlsx` 完成後，放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 並更新 `docs/abstracts_index.json`（取代測試資料）。

## ⚠️ 注意事項
- 目前 `docs/abstracts_index.json` 仍為第 59 次年會之測試資料，正式上線前務必置換為 2027 AACRT 正式資料。

## 🕐 最後更新
- 時間：2026-11-13 11:50
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
