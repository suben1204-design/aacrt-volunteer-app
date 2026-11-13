# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「Excel 清晰測試檔提煉（217 篇論文）與前端檢索介面全功能升級」：
1. **成功自 Excel 提煉 217 篇測試論文資料**：
   - 來源檔案：`創作庫-內部原創層/1、論文集/第59次年會暨國際醫學影像學術研討會 excel-測試用/` 內的兩份 Excel（由 Google 試算表匯出）。
   - 解析成果：口頭發表 74 篇（含會議室、精確時段、發表者、座長、論文題目）；壁報發表 143 篇（含論文編號、領域分類、發表者、論文題目）。
   - 正規化專題領域：`MR` (21), `OT` (41), `RO` (12), `NM` (8), `RT` (23), `AI` (14), `US` (2), `CT` (16), `CA` (11), `ST` (55), `IR` (7), `MA` (7)。
2. **生成結構化資料庫與快取**：
   - 更新 `知識庫-AI 提煉層/test_abstracts_benchmark.json`（純文字結構化資料庫）。
   - 更新 `docs/abstracts_index.json`（前端公開快取，共 217 篇完整結構）。
3. **前端介面與「Show-to-Guest」四語展示升級**：
   - 口頭與壁報以琥珀色/藍綠色清晰徽章區隔。
   - 口頭論文完整顯示演講場地（如 `303a 會議室`）、時間（如 `13:00-13:10`）與報告者。
   - 壁報論文統一顯示 `1F 海報展區` 與交流時段（`12:30-13:30`）。
   - 「秀給外賓」全螢幕卡片支援演講地點、時間、講者與類別四語對照。
   - 專題膠囊滾動列與多語系標籤字典（`zh-TW`/`en`/`ja`/`ko`）精確連動 217 篇計數。
4. **線上正式發布**：
   - PWA 快取版本推進至 `aacrt-guide-v2.11`。
   - 已推送至 GitHub Pages（commit `29fdc2e`），線上環境（HTTP 200 OK）已實時生效。
   - 再次確認：目前所有 2027 AACRT 正式論文與大會手冊皆尚未上傳，目前系統為乾淨測試狀態，未來正式 Excel 放入 `創作庫-內部原創層/1、論文集/2027 AACRT/` 後可一鍵替換。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（已發布 GitHub Pages）。
- **當前大腦版本**：`大腦 v1.08`（PWA Cache: `aacrt-guide-v2.11`）
- **論文測試基準庫**：`docs/abstracts_index.json`（共 217 篇論文完整索引）
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
- **GAS 部署 ID**：`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`（版本 `@9`）

## ➡️ 下一步可做事項
1. **實機手機 PWA 測試**：使用手機瀏覽器開啟線上網址，測試 217 篇論文之「分類標籤切換」、「口頭/壁報檢索」、「秀給外賓大字體」與四語朗讀。
2. **正式 2027 資料無縫升級**：待大會籌備處提供 `Excel-口頭--2027 AACRT.xlsx` 與 `Excel-Poster--2027 AACRT.xlsx`，放入 `2027 AACRT/` 目錄後即可一鍵置換為正式資料。

## 🕐 最後更新
- 時間：2026-11-13 08:56
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
