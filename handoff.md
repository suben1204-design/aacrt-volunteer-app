# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
完成第四階段「正式 Google 試算表即時連動」與「緊急跑馬燈與提問監控後台」全自動化串接：
1. **Google 試算表母本全面綁定**：
   - 試算表網址：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
   - 試算表 ID：`1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc`
2. **Google Apps Script 後端升級與權限設定**：
   - 設定 `appsscript.json` 之 `access: "ANYONE_ANONYMOUS"`，免登入公開即時同步。
   - `Code.js` 內建自動建立工作表機制：
     - 工作表一：`大會設定與跑馬燈`（修改 B1 即可即刻變更頂部跑馬燈公告；修改 B2 可調整大腦版本）
     - 工作表二：`即時提問紀錄`（自動非同步記錄現場提問、發問語言、來源、AI 回覆摘要，並具備特殊急迫狀況 🚨 幹部通報警報）
   - 部署更新至 Version 7（Deployment ID: `AKfycbwfbtyYhEHFLLLSlETnYbIdvsiFcXbRHDk-fG9NkUm_SbAvhscSGAd6-lWXcXjk5wLgBw`）。
3. **前端自動輪詢機制（60秒自動同步）**：
   - `index.html` 載入時自動透過 `fetchLiveTicker()` 向 Google 試算表抓取最新公告，並每 60 秒非同步自動輪詢一次，讓全場志工與外賓手機永遠顯示大會最新公告！
   - 底部版本號支援動態隨試算表 B2 欄位連動。
4. **Git 與 GitHub Pages 部署**：
   - 程式碼已更新並推送至 `main` 分支，GitHub Pages 已同步生效。

## 🚦 目前狀態
- **線上正式網址**：`https://suben1204-design.github.io/aacrt-volunteer-app/`（已同步至 GitHub Pages）。
- **Google 試算表後台**：`https://docs.google.com/spreadsheets/d/1IRhviHHTulLPx2ZXL25JD-8NgBCWGIU9HLyOO7CHjjc/edit`
- **架構健全度**：100% 串接完成，只要主管或幹部在試算表 B1 打字，所有手機 60 秒內立即同步更新！

## 🕐 最後更新
- 時間：2026-11-12 11:32
- 更新者：Antigravity @ FENGYI
- Git push：✅ 已推（main）
