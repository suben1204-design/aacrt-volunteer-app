# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「AACRT-志工APP工具」從 0 到 1 建置、7 輪 RDQ 規格定案與階段一至四核心交付：
1. **多語言大腦知識庫（`aacrt_brain.json` v1.3）**：收錄交通動線、南港 2 館會議室、全館 Wi-Fi、周邊生活換匯，並完整植入四大國際學術公版（試片室 704 室、A0 直式海報展區、學分感應與出席證明、大會晚宴接駁）、AACRT 放射四語專屬字典、GDPR 個資保護，以及「三層遞進式國際禮賓外交哲學（含大會延伸需求善意寬容推定原則）」。
2. **雙用官方 Web App（`index.html`）**：完成皇家海軍藍×琥珀金設計、頂部四語即時切換、Taipei Time (GMT+8) 即時時鐘、Google Noto Sans CJK 萬國字體、60/40 雙分頁、志工「Show-to-Guest 全螢幕大字體 ＋ 日/韓/英三語發音朗讀」、4 秒防刷冷卻、單人 20 次安全上限，以及 2027/04/26 12:00 自動落日關閉與閉幕感謝卡。
3. **PWA 離線快取（`sw.js` v1.3）**：Network-First 機制，大腦更新連網自動刷新，弱網離線可瀏覽核心資料。
4. **創作庫自動化流水線**：建立 `_archive/` 舊檔自動封存防衝突機制，以及 `scripts/compile_brain.py` 一鍵自動提煉編譯腳本。
5. **實體印刷對接**：於 `產出-成果層/` 產出大會志工識別證背卡專用尺寸向量檔 `AACRT_志工識別證背卡_QRCode.svg`。
6. **Git 與 GitHub**：全部程式碼與規格已推送至 `suben1204-design/aacrt-volunteer-app`。

## 🚦 目前狀態
- **本機原型與大腦離線功能 100% 可直接運行體驗**。
- 專案規格、防濫用、預算防護牆（$50 美元）、自動落日與學術大腦全部封頂，隨時可啟動階段五雲端後端串接。

## ➡️ 下一步
1. 建立獨立 Google 試算表「2027 AACRT 現場問答監控儀表板」，並編寫 Google Apps Script 雲端中繼程式碼（負責接收提問、非同步寫入試算表、遇特殊求助時以 LINE Messaging API 推播至志工幹部群組）。
2. 將前端 Web App 正式對接 GAS 端點，並部署至 GitHub Pages 對外發布。
3. 提供 Google Cloud / AI Studio 之 $50 美元硬性預算配額設定圖解操作指引。

## ⚠️ 注意事項
- 本專案 GitHub repo 為 **PRIVATE（私有）**。
- 未來隨時可將任何 Word/Excel/PDF 丟入 `創作庫-內部原創層/`，執行 `python scripts/compile_brain.py` 或呼叫 Agent 即可自動提煉更新。

## 🕐 最後更新
- 時間：2026-11-11 22:32
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
