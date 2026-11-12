# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「舊 TEST 論文資料徹底清理與等待 Google Sheet 上傳重置」：
1. **清理舊 TEST 資料**：
   - 舊版拆分測試 PDF（口頭與 POSTER）已自創作庫移除。
   - 知識庫 `test_abstracts_benchmark.json` 與公開快取 `docs/abstracts_index.json` 已重置清空（0 篇），徹底清除模糊 PDF 萃取的舊資料，避免與未來 2027 正式資料錯亂。
2. **前端檢索介面重置為待命狀態**：
   - 卡片 4 論文檢索計數重置為 0 篇，畫面友善提示「等待上傳最新整理論文資料 (Google Sheets)」。
3. **資料隔離與純淨保證**：
   - 再次確認：目前所有 2027 AACRT 正式論文與大會手冊皆尚未上傳，目前系統為純淨狀態，絕不混淆。
4. **線上正式發布**：
   - 已推送至 GitHub Pages（commit 88e1c45），線上環境已同步清空舊測試資料。

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
