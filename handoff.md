# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成「大腦 v1.06 升級、題庫順序修復、海報專區擴充與全語系連動」：
1. **修正 AI 本地題庫順序（解決第 2 題提前攔截 Bug）**：
   - 將原第 2 題（7樓會議室地圖）移至所有具體主題（洗手間、Keynote、CT/MRI/AI專題分廳、試片室、便當、晚宴、Wi-Fi、禁菸、學分、交通、海報）的最後一個順位，並移除 `怎麼走`，徹底解決英文提問與交通問題被誤判提前攔截的 Bug。
2. **擴充英/日/韓自然語言關鍵字 ＆ 新增「第 12 題：海報論文展區 (Poster Session)」**：
   - 擴充第 4 題（試片室）、第 7 題（Wi-Fi）、第 10 題（交通指引）之日韓文與英文關鍵字。
   - 新增第 12 題壁報展區（1樓展區、每日 12:30～13:30 交流評選）四語完整回答。
   - 校正第 2 題韓文漢字錯字（`고海상도` 修正為 `고해상도`）。
3. **修復「我的行程與收藏」多語系連動**：
   - 更新「我的收藏」標籤（`#my-favorites-label`），切換語系時保留星號數字（如 `★ 我的收藏 (0)` / `★ My Favorites (0)`）。
   - 議程清單與進行中演講卡片非中文語系自動顯示 `room_en`（例如 `Plenary Hall (7F)`、`Room 701 (CT/IVR)`、`1F Poster Area`），並動態切換 `地點：` / `Venue: ` / `場所：` / `장소: `。
4. **補齊跑馬燈與標籤 i18n 完整切換**：
   - 預設跑馬燈（`#ticker-text`）、會場指引標籤（`#header-guide-tag`）、地圖縮放提示等全部納入四國語言字典切換。
5. **版本遞增與 Google 試算表同步升級**：
   - 版本推進至 **大腦 v1.06**，PWA Cache 升級為 `aacrt-guide-v2.08`。
   - Google Apps Script 雲端後台已部署至 `@9` 版，自動將試算表升級為 `v1.06`，經 REST 呼叫實測成功。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（已同步至 GitHub Pages）。
- **當前大腦版本**：`大腦 v1.06`（PWA Cache: `aacrt-guide-v2.08`）
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
- **GAS 部署 ID**：`AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`（版本 `@9`）

## ➡️ 下一步可做事項
1. **實地會場模擬測試**：志工或外國學者可開啟手機瀏覽器加入主畫面，實測英文/日文/韓文語音提問與 Show-to-Guest 大字體朗讀功能。
2. **後續資料擴充**：若大會 2027 手冊正式定稿，可將正式 PDF/JPG 置入 `docs/` 資料夾取代占位檔。

## 🕐 最後更新
- 時間：2026-11-12 13:09
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main，commit `ec8fad8`）
