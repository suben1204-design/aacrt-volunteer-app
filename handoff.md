# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成 RDQ 規格交棒與第一版原型核心交付，並完成「階段一至階段三」現場關鍵盲點補強：
1. **多語言大腦資料庫（`aacrt_brain.json` v1.1）**：
   - 增加版本管理（`v1.1`）與自動刷新機制。
   - 內嵌 **AACRT 放射專門四語術語字典（Glossary）**（醫事放射師/診療放射線技師/방사선사/RT、CT、MRI、輻射防護、IVR、超音波、AI 影像）。
   - 嚴格落實 **GDPR 與個資隱私防線**，嚴禁外洩講者私人電話與飯店房號。
2. **雙用官方 Web App（`index.html`）**：
   - 頂部整合 **Taipei Time (GMT+8) 即時時鐘**，解決日韓歐美外賓時差錯亂問題。
   - 導入 **Google Noto Sans CJK（繁中/日文/韓文）萬國字體**，杜絕外籍手機缺字掉字（豆腐塊）。
   - 底部顯示大腦版本徽章。
3. **PWA 快取機制（`sw.js` v1.1）**：採 Network-First 策略，大腦只要有更新，手機上網時自動無感覆蓋舊資料。
4. **Git 與 GitHub**：全部程式碼與資產已成功 Push 至 `suben1204-design/aacrt-volunteer-app`。

## 🚦 目前狀態
- **前端原型與本機大腦已可直接開啟預覽運作（包含四語切換與語音輸入）**。
- 準備進入後端 Google Apps Script 雲端中繼串接（Gemini Flash + Google Sheets 提問記錄）。

## ➡️ 下一步
1. 建立 Google Apps Script 後端中繼程式碼（負責接收提問、呼叫 Gemini Flash、回寫 Google Sheets）。
2. 將前端對話串接至 GAS Web App 端點，完成雲端全自動化。
3. 輸出 $50 美元預算配額設定指南與大會現場 QR Code 產出。

## ⚠️ 注意事項
- 本專案 GitHub repo 為 **PRIVATE（私有）**。
- 本地測試可直接以瀏覽器開啟 `index.html`，語音輸入建議在 Chrome 或 Safari 下點擊麥克風按鈕體驗。

## 🕐 最後更新
- 時間：2026-11-11 21:06
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
