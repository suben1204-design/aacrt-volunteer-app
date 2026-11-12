# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「大腦 v1.08 升級、大會擴充為 3 日（納入 4/23 Day 1 七大官方議程）、啟用學術論文摘要快速檢索卡」：
1. **大會日程擴充為 3 日（4/23 Day 1, 4/24 Day 2, 4/25 Day 3）**：
   - 根據使用者上傳之官方截圖（`2027 AACRT_1026.pdf` 第 1 頁），在 `CONFERENCE_SESSIONS` 資料庫完整納入 4/23 當天七大核心時段：
     - `09:00 - 12:00`: Section 1: 全人教育論壇 (Holistic Educational Forum, 702 ABC)
     - `09:00 - 12:00`: AACRT 國際理監事會議 (AACRT Board Meeting, 703 ABC)
     - `12:00 - 13:30`: 大會交流午餐 (Lunch & Networking, 7F 餐廳)
     - `13:30 - 16:30`: Section 2: 電腦斷層尖端工作坊 (CT Workshop, 702 ABC)
     - `13:30 - 16:30`: ISRRT 亞澳區區域代表會議 (ISRRT AA Regional Meeting, 703 ABC)
     - `16:30 - 17:30`: EACRT 東亞醫事放射學會理事會議 (EACRT Board Meeting, 703 ABC)
     - `18:30 - 20:30`: 2027 AACRT 歡迎晚宴暨會長之夜 (Welcome Banquet / Presidential Dinner)
   - 「我的行程」UI 增加 `4/23 (Day 1)`、`4/24 (Day 2)`、`4/25 (Day 3)` 與 `全部三日` 切換按鈕，支援四國語言與各時段模擬按鈕（增加 4/23 10:00 與 14:00 快速切換）。
   - 「現在進行中 (Happening Now)」邏輯升級：依據台北時間（`Asia/Taipei`）精準比對 4/23、4/24、4/25 當天時段。
2. **前端「大會文件 / 地圖」分頁啟用「論文摘要快速檢索卡 (Abstract Search)」**：
   - 於 `docs/abstracts_index.json` 建置 195 篇學術論文快取索引（130 KB，支援離線 PWA 快取）。
   - 支援 11 大專題領域快速切換膠囊按鈕（全部、AI、CT、MRI、放療 RT、核醫 NM、超音波 US、品管 QC、血管攝影 Angio、教育 Edu、其他 Other）。
   - 支援即時關鍵字模糊搜尋（論文編號如 `O-AI-001`、`P-CT-008`、論文題目、收錄頁碼或關鍵字），具備一鍵清除按鈕。
   - 每篇論文卡片提供「問 AI」一鍵帶入問題跳轉智慧對談，以及「秀給外賓」全螢幕四語 Show-to-Guest 大字體卡片。
3. **PWA 與版本演進**：
   - 大腦版本推進至 **v1.08**，PWA Service Worker 快取版本推進至 `aacrt-guide-v2.10`（納入 `./docs/abstracts_index.json` 離線預載）。
   - 在 `.gitignore` 明確隔離 95.9MB 之 2026 測試論文集 PDF，保障 GitHub 提交安全與純淨。

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
