# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「測試用資料清理與口頭/POSTER新拆分測試檔提煉更新」：
1. **清理舊 TEST 資料**：
   - 移除舊版 `115大會手冊_電子版0322.pdf` 與先前近 100MB 之大型測試 PDF，Git 歷史追蹤同步清理。
   - 更新 `.gitignore`，將 `創作庫-內部原創層/第59次年會暨國際醫學影像學術研討會-測試用/` 完整列入忽略名單，防範未來測試暫存檔誤入版本庫。
2. **提煉新拆分測試資料（217 篇論文）**：
   - 成功由 `第59次年會暨國際醫學影像學術研討會-測試用/` 的兩份 PDF 萃取出 217 篇論文（74 篇口頭發表、143 篇壁報發表）。
   - 更新結構化索引 `test_abstracts_benchmark.json` 與公開快取 `docs/abstracts_index.json`（標記為測試 Benchmark 專案，絕不污染 2027 AACRT 正式大腦）。
   - 前端 12 個專題分類膠囊標籤與計數全面同步更新（支援四語切換）。
3. **線上正式發布驗證**：
   - GitHub Pages 自動部署完成，`abstracts_index.json` 與 `index.html` 均回應 HTTP 200 OK。

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
