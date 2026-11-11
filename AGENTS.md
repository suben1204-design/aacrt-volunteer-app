# AACRT-志工APP工具（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
2027 年第 26 屆亞澳區醫事放射師學術國際會議（The 26th AACRT）與中華民國醫事放射學會第 60 次年會（TWSRT 60th Annual Meeting）之「多語言智慧大腦 Web App（PWA）」。為大會志工及外國來訪學者、學生提供零延遲會議資訊查詢（地點、時間、議程場次、會議室代號、交通與生活指引）、英/日/韓/繁中四國語言支援。架構採「60/40 混合式」（60% 快捷 FAQ + 40% Gemini Flash 智能對答），提問即時同步至 Google Sheets，未知問題精確導流至「大會諮詢台」，支援離線地圖快取與即時緊急跑馬燈，並附帶大會現場 Token 預先購置與不斷線評估。

- **線上網址（GitHub Pages）**：即將建立（預計 `https://suben1204-design.github.io/aacrt-volunteer-app/`）
- **GitHub 儲存庫**：https://github.com/suben1204-design/aacrt-volunteer-app（私有）

## 關鍵時程
- **大會日期**：2027 年 4 月 24 日（六）至 4 月 25 日（日）
- **大會地點**：台北南港展覽館 2 館（TaiNEX 2）

## 目標與路線圖
- [x] 階段一：完成 RDQ 需求探索訪談並依回饋完成修訂版規格卡（`revisions: 1`）
- [x] 階段二：完成 L1 本地標準骨架 + L2 GitHub 私有庫 + L3 Obsidian 駕駛艙初始化
- [ ] 階段三：建置多語言大會大腦資料結構（`知識庫-AI 提煉層/aacrt_brain.json`）與 60% 快捷 FAQ 資料
- [ ] 階段四：開發雙用官方版前端 Web App（皇家海軍藍×琥珀金風格、四語切換、PWA 離線快取、語音輸入）
- [ ] 階段五：串接 Google Apps Script 中繼與 Gemini Flash API，完成 Google Sheets 提問記錄與緊急跑馬燈廣播（未知問題導流至大會諮詢台）
- [ ] 階段六：實施 Token 預先購置與容量評估報告，完成實機測試與 GitHub Pages 發佈

## 資料夾結構
```text
AACRT-志工APP工具/
├── AGENTS.md                 # 跨 Agent 靜態專案藍圖與技術規範
├── handoff.md                # 跨電腦／跨 Agent 當下交接檔
├── .gitignore                # Git 忽略規則
├── Clipping-外部素材層/       # 外部參考（南港 2 館動線圖、北捷/機捷外語指引）
├── 創作庫-內部原創層/         # 大會官方議程、手冊草案、志工 SOP 母檔（神聖唯讀）
├── 知識庫-AI 提煉層/         # AI 提煉之大會精華大腦（aacrt_brain.json/md）
├── 產出-成果層/              # 交付成果、宣傳立牌 QR Code、導覽手冊輸出
├── assets/                   # 多媒體資產（images / audio / video）
└── rdq/                      # RDQ 需求探索規格卡（revisions: 1）
```

## 同步層級（本專案初始化至第 3 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（雲端硬碟資料夾） | `AGENTS.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | `suben1204-design/aacrt-volunteer-app`（私有） | 指定時 |
| L3 | Obsidian | `AACRT-志工APP工具/專案工作流程.md` | 有需要時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構

## 安全與隱私（不可違反）
- **不把 API key、密碼、憑證寫進 repo**，也不要貼進 `AGENTS.md`／`handoff.md`；一律放 `.env` 並列入 `.gitignore`
- **絕不讓外部 Web App 直接存取私人 Google Drive**，一律由 Agent 提煉成公開大腦後發布
