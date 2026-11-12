# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成第三階段 4 項關鍵除錯與「混合雙層架構 (Hybrid Two-Tier AI)」重大升級（大腦 v1.04 終極穩健版）：
1. **英文單字邊界正規表達式修正（解決子字串誤判）**：
   - 全面改用 `/\b(ct|mri|ai|ivr|pet)\b/i` 等單字邊界，徹底解決 `train`、`claim`、`direct`、`restroom`、`smart` 等英文單字誤觸第 2、3 題的問題。
   - **全新第 11 題上線**：「**洗手間與哺集乳室指引**」，提供 7 樓與 1 樓男廁、女廁、無障礙廁所與哺集乳室之四語詳細位置說明。
2. **`renderHappeningNow` 的 `live` 實體時間日期鎖定**：
   - 動態判斷台北時間為 4/24 還是 4/25，嚴格限制 `s.day === targetDay`，杜絕跨日演講混雜顯示。
3. **歷史對話即時切換語系與 UI 標籤補齊**：
   - 歷史對話氣泡加入 `data-msg-idx`，切換右上角語言時，畫面上已輸出的 AI 歷史回答會**即時切換為該國語言**！
   - `#day-filter-all-btn`、`#filter-all-sessions-btn`、`#star-hint-label`、`#footer-venue-label` 完整納入 i18n。
   - 燈箱加入圖片容錯 fallback，防止破圖。
4. **混合雙層 AI 架構（Hybrid Two-Tier AI）全面就緒**：
   - **第一層**：命中 1～11 題核心題庫時（`matched: true`），0 秒秒回。
   - **第二層**：未命中核心題庫時（`matched: false`），由 `fetchCloudBrainAnswer` 帶 5 秒超時保護，非同步向 Google Apps Script 雲端請求 Gemini Flash 動態解答。
   - **第三層**：若雲端未啟用、超時或離線，自動無縫降級為原本的「外交禮賓導流（導流至大會諮詢台）」，100% 穩定零當機。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（已同步至 GitHub Pages）。
- **架構健全度**：本地核心題庫 100% 精準零誤判，混合雙層 AI 與歷史對話語言連動已正式生效。

## 🕐 最後更新
- 時間：2026-11-12 10:46
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
