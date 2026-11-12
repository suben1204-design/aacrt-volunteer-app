# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「大腦 v1.08 升級、大會擴充為 3 日（納入 4/23 Day 1 七大官方議程）、啟用學術論文摘要快速檢索卡與關鍵 Bug 修復」：
1. **大會日程擴充為 3 日（4/23 Day 1, 4/24 Day 2, 4/25 Day 3）**：
   - 根據使用者上傳之官方截圖（`2027 AACRT_1026.pdf` 第 1 頁），在 `CONFERENCE_SESSIONS` 資料庫完整納入 4/23 當天七大核心時段（全人教育論壇、AACRT 理監事會、交流午餐、CT 工作坊、ISRRT 亞澳區會議、EACRT 理事會議、歡迎晚宴／會長之夜）。
   - 「我的行程」UI 增加 `4/23 (Day 1)`、`4/24 (Day 2)`、`4/25 (Day 3)` 與 `全部三日` 切換按鈕，支援四國語言與各時段模擬按鈕（增加 4/23 10:00 與 14:00 快速切換）。
   - 「現在進行中 (Happening Now)」邏輯升級：依據台北時間（`Asia/Taipei`）精準比對 4/23、4/24、4/25 當天時段。
   - 首頁焦點看板右上角日期已統一修正為 `2027/04/23 - 04/25`。
2. **前端「大會文件 / 地圖」分頁啟用「論文摘要快速檢索卡 (Abstract Search)」與關鍵除錯**：
   - 於 `docs/abstracts_index.json` 建置 195 篇學術論文快取索引（130 KB，支援離線 PWA 快取）。
   - 修復 `#abstract-results-list` DOM 容器 ID 不一致與 `.abs-cat-btn` / `data-cat` 屬性不一致，確保論文卡片順暢渲染與專題膠囊高亮切換。
   - 修復「秀給外賓」呼叫未定義函式問題，改存入 `messageStore` 並調用 `showToGuestFromStore`，四語大字體卡片與語音朗讀 100% 正常。
   - 在 `generateLocalBrainAnswerBundle` 優先攔截 `[論文編號]` 格式（如 `[O-AI-001]`），直接回覆收錄頁碼與論文發表指引，避免題目含 CT/AI 誤觸分廳問題。
   - 在 `updateLanguageUI` 補齊 11 大論文專題分類按鈕多語系切換標籤。
3. **擴充晚宴與會場地址資訊**：
   - 第 6 題擴充涵蓋 4/23 歡迎晚宴（18:30-20:30）與 4/24 大會晚宴（18:30-21:00，南港 2 館 1 樓備有接駁車）。
   - 第 10 題補上南港 2 館官方中英文地址（`台北市南港區經貿二路2號 / No. 2, Jingmao 2nd Rd., Nangang Dist., Taipei`）與桃園機場捷運接駁指引。
4. **PWA 與版本演進**：
   - 大腦版本推進至 **v1.08**，PWA Service Worker 快取版本推進至 `aacrt-guide-v2.10`（納入 `./docs/abstracts_index.json` 離線預載）。
   - GitHub Pages 正式發布驗證通過（HTTP 200 OK）。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（已發布 GitHub Pages）。
- **當前大腦版本**：`大腦 v1.08`（PWA Cache: `aacrt-guide-v2.10`）
- **論文測試基準庫**：`知識庫-AI 提煉層/test_abstracts_benchmark.json` 與 `docs/abstracts_index.json`（共 195 篇論文索引）
- **論文提煉腳本**：`scripts/test_abstract_pipeline.py`
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
- **GAS 部署 ID**：`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`（版本 `@9`）

## ➡️ 下一步可做事項
1. **論文集正式定稿置換**：待大會籌備處提供 2027 年 AACRT 正式論文集後，放入 `創作庫-內部原創層/`，執行提煉腳本即可無縫更新。
2. **實機手機 PWA 測試**：使用手機 Safari / Chrome 開啟線上網址，測試「加入主畫面」、離線檢索論文、三日行程收藏與四語朗讀。

## 🕐 最後更新
- 時間：2026-11-12 15:15
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
