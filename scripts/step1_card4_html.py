# -*- coding: utf-8 -*-
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. 替換 HTML 中的 卡片 4
# ---------------------------------------------------------------------------
card4_old = '''      <!-- 卡片 4：論文摘要快速檢索卡 (Scientific Abstracts Search) -->
      <div id="abstract-search-card" class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 hover:shadow-md transition-shadow">
        <div class="flex items-start space-x-3 mb-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-50 text-cyan-700 flex items-center justify-center shrink-0 mt-0.5 border border-cyan-100">
            <i class="fa-solid fa-microscope text-lg"></i>
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <h3 id="abstract-card-title" class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
                <span>4、學術論文摘要即時檢索 (Abstract Search)</span>
              </h3>
              <span id="abstract-indexed-badge" class="text-[10px] bg-cyan-100 text-cyan-900 font-bold px-2 py-0.5 rounded-full border border-cyan-200">
                195 篇論文已索引
              </span>
            </div>
            <p id="abstract-card-desc" class="text-xs text-slate-600 mt-1 leading-relaxed">
              即時檢索口頭與壁報論文。支援專題領域（CT、MRI、AI、放療等）、論文編號（如 P-CT-008、O-AI-001）或關鍵字。
            </p>
          </div>
        </div>

        <!-- 搜尋列 -->
        <div class="relative flex items-center mb-2.5">
          <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
          <input id="abstract-search-input" type="text" oninput="handleAbstractSearch(this.value)" placeholder="輸入論文編號、題目或關鍵字 (如 CT, AI, PSMA, 劑量)..." class="w-full pl-8 pr-8 py-2 bg-slate-50 border border-slate-200 focus:border-cyan-500 focus:bg-white rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none transition-all font-medium">
          <button id="abstract-clear-btn" onclick="clearAbstractSearch()" class="hidden absolute right-2.5 w-4 h-4 rounded-full bg-slate-300 text-white hover:bg-slate-400 flex items-center justify-center text-[9px]">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- 專題快速標籤列 (Horizontal Scroll Pills) -->
        <div class="flex items-center space-x-1.5 overflow-x-auto no-scrollbar pb-1 mb-3 text-[11px]">
          <button onclick="filterAbstractCategory('ALL')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-800 text-cyan-300 shrink-0 shadow-sm transition-all" data-cat="ALL">全部 (217)</button>
          <button onclick="filterAbstractCategory('AI')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="AI">AI 人工智慧 (14)</button>
          <button onclick="filterAbstractCategory('CT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="CT">CT 電腦斷層 (16)</button>
          <button onclick="filterAbstractCategory('MR')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="MR">MRI 磁振造影 (21)</button>
          <button onclick="filterAbstractCategory('RT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="RT">RT 放射治療 (23)</button>
          <button onclick="filterAbstractCategory('NM')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="NM">NM 核子醫學 (8)</button>
          <button onclick="filterAbstractCategory('CA')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="CA">CA 心導管 (11)</button>
          <button onclick="filterAbstractCategory('IR')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="IR">IR 血管介入 (7)</button>
          <button onclick="filterAbstractCategory('MA')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="MA">MA 乳房攝影 (7)</button>
          <button onclick="filterAbstractCategory('RO')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="RO">RO 常規X光 (12)</button>
          <button onclick="filterAbstractCategory('US')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="US">US 超音波 (2)</button>
          <button onclick="filterAbstractCategory('ST')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="ST">ST 學生研究 (55)</button>
          <button onclick="filterAbstractCategory('OT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="OT">OT 綜合其他 (41)</button>
        </div>

        <!-- 檢索結果列表 (預設顯示焦點精選，搜尋時動態更新) -->
        <div id="abstract-results-header" class="flex items-center justify-between text-[11px] text-slate-500 mb-1.5 px-0.5">
          <span id="abstract-result-count">焦點論文推薦：</span>
          <span id="abstract-hint-click" class="text-[10px] text-slate-400">點擊卡片查閱摘要詳情</span>
        </div>
        <div id="abstract-results-list" class="space-y-2 max-h-80 overflow-y-auto no-scrollbar pr-0.5">
          <!-- Rendered dynamically by JavaScript -->
        </div>
      </div>'''

card4_new = '''      <!-- 卡片 4：論文摘要即時檢索 (Abstract Search) - 雙分頁重構架構 -->
      <div id="abstract-search-card" class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 hover:shadow-md transition-shadow">
        <!-- 區塊標題與統計徽章 -->
        <div class="flex items-start space-x-3 mb-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-50 text-cyan-700 flex items-center justify-center shrink-0 mt-0.5 border border-cyan-100 shadow-xs">
            <i class="fa-solid fa-microscope text-lg"></i>
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <h3 id="abstract-card-title" class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
                <span>4、學術論文摘要即時檢索 (Abstract Search)</span>
              </h3>
              <span id="abstract-indexed-badge" class="text-[10px] bg-cyan-100 text-cyan-900 font-bold px-2 py-0.5 rounded-full border border-cyan-200">
                217 篇論文已索引
              </span>
            </div>
            <p id="abstract-card-desc" class="text-xs text-slate-600 mt-1 leading-relaxed">
              即時檢索口頭與海報發表論文。請切換下方分頁，輸入「論文編號」或「報告者姓名」進行精準篩選。
            </p>
          </div>
        </div>

        <!-- 兩大獨立查詢區分頁切換列 (Oral vs Poster Tabs) -->
        <div class="flex items-center p-1 bg-slate-100 rounded-xl mb-3 border border-slate-200/80">
          <button id="abs-tab-oral" onclick="switchAbstractTab('oral')" class="flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 shadow-sm bg-white text-cyan-900 border border-slate-200">
            <i class="fa-solid fa-chalkboard-user text-amber-600"></i>
            <span id="abs-tab-oral-label">1、口頭發表 (Oral)</span>
            <span id="abs-oral-badge" class="ml-1 text-[10px] bg-amber-100 text-amber-900 px-1.5 py-0.2 rounded-full font-sans font-bold">74</span>
          </button>
          <button id="abs-tab-poster" onclick="switchAbstractTab('poster')" class="flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 text-slate-600 hover:text-slate-900">
            <i class="fa-solid fa-image text-cyan-600"></i>
            <span id="abs-tab-poster-label">2、海報發表 (Poster)</span>
            <span id="abs-poster-badge" class="ml-1 text-[10px] bg-cyan-100 text-cyan-900 px-1.5 py-0.2 rounded-full font-sans font-bold">143</span>
          </button>
        </div>

        <!-- 1. 口頭發表查詢專區 (Oral Presentation Panel) -->
        <div id="abs-oral-panel" class="space-y-2.5">
          <!-- 搜尋列 -->
          <div class="relative flex items-center">
            <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
            <input id="abstract-oral-search-input" type="text" oninput="handleOralSearch(this.value)" placeholder="輸入論文編號或報告者姓名 (如 O-NMR-01, 陳大同)..." class="w-full pl-8 pr-8 py-2 bg-slate-50 border border-slate-200 focus:border-cyan-500 focus:bg-white rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none transition-all font-medium">
            <button id="abstract-oral-clear-btn" onclick="clearOralSearch()" class="hidden absolute right-2.5 w-4 h-4 rounded-full bg-slate-300 text-white hover:bg-slate-400 flex items-center justify-center text-[9px]">
              <i class="fa-solid fa-xmark"></i>
            </button>
          </div>

          <!-- 結果計數與提示 -->
          <div class="flex items-center justify-between text-[11px] text-slate-500 px-0.5">
            <span id="abstract-oral-count" class="font-bold text-slate-700">顯示 74 篇口頭發表</span>
            <span class="text-[10px] text-slate-400 flex items-center gap-1">
              <i class="fa-solid fa-circle-info text-amber-500"></i>
              <span id="abstract-oral-hint">完整列出 6 項發表資訊</span>
            </span>
          </div>

          <!-- 口頭發表清單容器 -->
          <div id="abstract-oral-list" class="space-y-2.5 max-h-80 overflow-y-auto no-scrollbar pr-0.5">
            <!-- Rendered dynamically by JavaScript -->
          </div>
        </div>

        <!-- 2. 海報發表查詢專區 (Poster Presentation Panel) -->
        <div id="abs-poster-panel" class="hidden space-y-2.5">
          <!-- 搜尋列 -->
          <div class="relative flex items-center">
            <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
            <input id="abstract-poster-search-input" type="text" oninput="handlePosterSearch(this.value)" placeholder="輸入論文編號或報告者姓名 (如 P-AI-001, 吳怡萱)..." class="w-full pl-8 pr-8 py-2 bg-slate-50 border border-slate-200 focus:border-cyan-500 focus:bg-white rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none transition-all font-medium">
            <button id="abstract-poster-clear-btn" onclick="clearPosterSearch()" class="hidden absolute right-2.5 w-4 h-4 rounded-full bg-slate-300 text-white hover:bg-slate-400 flex items-center justify-center text-[9px]">
              <i class="fa-solid fa-xmark"></i>
            </button>
          </div>

          <!-- 結果計數與提示 -->
          <div class="flex items-center justify-between text-[11px] text-slate-500 px-0.5">
            <span id="abstract-poster-count" class="font-bold text-slate-700">顯示 143 篇海報發表</span>
            <span class="text-[10px] text-slate-400 flex items-center gap-1">
              <i class="fa-solid fa-location-dot text-cyan-600"></i>
              <span id="abstract-poster-hint">展區：1F 海報展區 (12:30-13:30 交流)</span>
            </span>
          </div>

          <!-- 海報發表清單容器 -->
          <div id="abstract-poster-list" class="space-y-2 max-h-80 overflow-y-auto no-scrollbar pr-0.5">
            <!-- Rendered dynamically by JavaScript -->
          </div>
        </div>
      </div>'''

assert card4_old in html, "card4_old not found in index.html"
html = html.replace(card4_old, card4_new)
print("Step 1 SUCCESS: Card 4 HTML replaced.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
