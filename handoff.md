# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「AACRT-志工APP工具」新專案建立與三層級初始化：
1. **RDQ 規格定案**：完成需求探索訪談，已確認採「雙用大會官方版」+「80/20 混合式問答（快捷 FAQ + Gemini Flash）」+「四國語系切換」+「PWA 離線地圖」+「Google Sheets 跑馬燈與提問紀錄」。規格卡落檔於 `rdq/RDQ-spec-aacrt-smart-guide-app-20261111.md`。
2. **L1 本地骨架**：於 `G:\我的雲端硬碟\100、AI\02、projects\AACRT-志工APP工具` 建立五大標準目錄（外部素材層、內部原創層、AI 提煉層、產出成果層、多媒體 assets）。
3. **L2 GitHub 私有庫**：建立並推上 `suben1204-design/aacrt-volunteer-app`。
4. **L3 Obsidian 駕駛艙**：於 `110、Obsidian\fengyi\專案\AACRT-志工APP工具\` 建立 `專案工作流程.md`。

## 🚦 目前狀態
- **專案基礎建設已完全就緒（第 3 層級）**。
- 專案骨架與版本控制已綁定，準備進入大會大腦資料結構設計與前端開發。

## ➡️ 下一步
1. 於 `知識庫-AI 提煉層/` 建立第一版大會多語言大腦結構檔（`aacrt_brain.json`，涵蓋南港 2 館會議室、交通指引、常用 FAQ）。
2. 開發前端雙用 Web App 原型（`index.html`），具備皇家海軍藍×琥珀金風格、頂部四語切換、快捷摺疊卡片。
3. 規劃 Google Apps Script 串接端點以處理 Gemini API 轉發與試算表記錄。

## ⚠️ 注意事項
- 本專案 GitHub repo 為 **PRIVATE（私有）**，日後若需啟用 GitHub Pages 請注意切勿將任何未加密 API Key 寫入前端 HTML/JS。
- 大會原始資料放在 `創作庫-內部原創層/`，Web App 僅讀取 Agent 提煉後的公開大腦，嚴禁讓外部直接存取 Drive。

## 🕐 最後更新
- 時間：2026-11-11 20:54
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
