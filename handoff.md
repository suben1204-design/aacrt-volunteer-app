# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
已全面完成專案路線圖的**階段五（Google Apps Script 雲端中繼儀表板）**、**階段六（GitHub Pages 正式上線公開發布）**，以及**使用者回饋之 UI 全面重構與場地空間規格建檔**：
1. **GitHub Pages 線上版本全新重構升級（v2.0-clean）**：
   - 線上正式網址：`https://suben1204-design.github.io/aacrt-volunteer-app/`（HTTP 200 OK，PWA 離線快取更新為 Network-First）。
   - GitHub 儲存庫：`suben1204-design/aacrt-volunteer-app`。
   - **UI 重大升級亮點**：
     - **去除技術術語**：徹底移除底部「預算防護 $50 Cap / PWA 離線支援」等工程字樣，頁面俐落清爽。
     - **頁籤更名與純淨化**：改為直覺正式的「常見 Q&A」與「智慧對談」；修復切換繁體中文時卡片標題語言顯示 Bug。
     - **學術與會場核心 Q&A**：置頂南港 2 館 7 樓會議空間總覽卡片，收斂為 4 大核心模組（議程演講、試片海報、便當晚宴、學分法規）。
     - **智慧對談大輸入區**：語音麥克風與送出鈕放大為 48×48px，文字輸入框加大加寬，提升行動裝置與現場長者操作體驗。
     - **熱門提問精選 6 題 + 試算表即時連線**：精選 6 大實用情境卡片，並透過 Google Apps Script 動態抓取現場最常被問的高頻熱搜題目（`🔥 現場大會熱搜中`）。
2. **Google Apps Script 雲端中繼部署完成（Web App）**：
   - 專案名稱：`2027 AACRT 現場問答監控儀表板`
   - 端點網址：`https://script.google.com/macros/s/AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw/exec`
   - 功能：非同步提問日誌寫入、即時跑馬燈公告同步、緊急特殊求助警報（發信至 `suben1204@gmail.com`）、熱門高頻問題即時回傳統計。
3. **場地空間規格與測試資料庫建立**：
   - 已在 `創作庫-內部原創層/` 建檔《南港展覽館2館7樓會議室空間規格與配置.md》（詳載 701、702、703、704、705 會議室尺寸、挑高與容納人數）。
   - 已安全歸檔 `115大會手冊_電子版0322.pdf`（僅作為流程測試用途，實施嚴格隔離，絕不污染 2027 AACRT 正式大腦）。

## 🚦 目前狀態
- **專案進度**：核心功能與介面全數交付完畢，狀態為隨時可對外展示與實測。
- **Git 狀態**：本地與遠端 `origin/main` 完全同步，所有 PDF、JPG 與原始碼均已安全推送到 GitHub。

## ➡️ 接續工作指引
- 當大會籌備委員會提供 2027 AACRT 正式手冊或議程定案時，放入 `創作庫-內部原創層/` 並運行 `scripts/compile_brain.py` 更新大腦版本即可。

## 🕐 最後更新
- 時間：2026-11-12 00:46
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
