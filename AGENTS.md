# AACRT-志工APP工具（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
2027 年第 26 屆亞澳區醫事放射師學術國際會議（The 26th AACRT）與中華民國醫事放射學會第 60 次年會（TWSRT 60th Annual Meeting）之「多語言智慧大腦 Web App（PWA）」。為大會志工及外國來訪學者、學生提供零延遲會議資訊查詢（地點、時間、議程場次、會議室代號、試片室、海報展區、學分證明、晚宴接駁、交通與生活指引）、英/日/韓/繁中四國語言支援。架構採「60/40 混合式」（60% 快捷 FAQ + 40% Gemini Flash 智能對答），提問即時同步至獨立監控 Google Sheets，特殊求助推播至 LINE 幹部群組，具備「三層遞進式國際禮賓外交哲學」與善意寬容推定原則，未知問題精確導流至「大會諮詢台」，支援離線地圖快取、Show-to-Guest 全螢幕大字體三語朗讀，並在後端設定 $50 美元預算上限防護牆與 2027/04/26 12:00 自動落日關閉機制。

- **線上網址（GitHub Pages）**：https://suben1204-design.github.io/aacrt-volunteer-app/
- **GitHub 儲存庫**：https://github.com/suben1204-design/aacrt-volunteer-app（公開發佈 Pages）

## 關鍵時程
- **大會日期**：2027 年 4 月 24 日（六）至 4 月 25 日（日）
- **大會地點**：台北南港展覽館 2 館（TaiNEX 2）
- **落日截止**：2027 年 4 月 26 日（一）12:00 準時自動停止服務並轉為閉幕紀念頁

## 目標與路線圖
- [x] 階段一：完成 RDQ 需求探索訪談並鎖定 $50 美元預算防護牆與善意寬容原則（`revisions: 9`，含禁菸法規與過敏領餐）
- [x] 階段二：完成 L1 本地標準骨架 + L2 GitHub 私有庫 + L3 Obsidian 駕駛艙初始化
- [x] 階段三：建置多語言大會大腦（`aacrt_brain.json` v1.5，含四大國際學術公版、八大營運實務模組、放射四語字典、GDPR 規範、台北時鐘、CJK 萬國字體）、創作庫自動封存夾 `_archive/` 與一鍵提煉腳本 `scripts/compile_brain.py`
- [x] 階段四：開發雙用官方版前端 Web App（`index.html`，具備 60/40 雙分頁、四語切換、語音輸入、「Show-to-Guest 三語即時朗讀」、防刷冷卻、救命級禁菸/過敏快速過濾與 2027/04/26 自動落日感謝卡），並於 `產出-成果層/` 產出名牌背卡 QR Code 向量印刷檔
- [x] 階段五：建置獨立 Google 試算表與 GAS 雲端中繼（提問非同步記錄、即時跑馬燈同步、特殊求助推播通報）
- [x] 階段六：完成 GitHub Pages 正式發佈（https://suben1204-design.github.io/aacrt-volunteer-app/），並提供 $50 美元預算配額硬性防護牆設定指引
- [x] 階段七：全面重構升級大腦 v1.04（大會核心文件專區、會場地圖雙指縮放燈箱、個人化行程收藏與當前進行中動態卡片、混合雙層 AI 架構、英文單字邊界防誤判與歷史對話即時四語切換）

## 資料夾結構
```text
AACRT-志工APP工具/
├── AGENTS.md                          # 跨 Agent 靜態專案藍圖與技術規範
├── handoff.md                         # 跨電腦／跨 Agent 當下交接檔
├── index.html                         # 雙用官方 Web App 前端（四語/語音/Show to Guest/雙指縮放/混合雙層AI）
├── manifest.json                      # PWA 設定檔
├── sw.js                              # PWA Service Worker 離線快取（v2.06）
├── .gitignore                         # Git 忽略規則
├── docs/                              # 前端展示用實體檔案目錄（總議程PDF、地圖JPG/PDF、手冊PDF）
│   ├── 1_agenda.pdf
│   ├── 2_floor_map.pdf
│   ├── 2_floor_map_7f.jpg
│   └── 3_handbook.pdf
├── scripts/
│   └── compile_brain.py               # 創作庫多檔案一鍵自動提煉編譯腳本（含舊版歸檔）
├── Clipping-外部素材層/                # 外部參考（南港 2 館動線圖、北捷/機捷外語指引）
├── 創作庫-內部原創層/                  # 大會官方議程、手冊草案、志工 SOP 母檔（神聖唯讀）
│   ├── 常見 Q&A」/                    # 使用者即時置放與更新之大會最新原檔母庫
│   └── _archive/                      # 舊版本自動封存區（防版本衝突）
├── 知識庫-AI 提煉層/                  # AI 提煉之大會精華大腦（aacrt_brain.json v1.04）
├── 產出-成果層/                       # 交付成果、名牌背卡 QR Code 向量印刷圖檔
├── assets/                            # 多媒體資產（images / audio / video）
└── rdq/                               # RDQ 需求探索規格卡
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
