# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. 替換 HTML：卡片 4 改為上下兩個完全獨立的查詢專區
# ---------------------------------------------------------------------------
old_html_start = '      <!-- 卡片 4：論文摘要即時檢索 (Abstract Search) - 雙分頁重構架構 -->'
idx_html_start = html.find(old_html_start)
idx_html_end = html.find('<!-- 諮詢台聯絡卡片 -->', idx_html_start)
assert idx_html_start != -1 and idx_html_end != -1, "Card 4 HTML block not found"

new_card4_html = '''      <!-- 卡片 4：論文摘要即時檢索 (Abstract Search) - 雙獨立專區架構 -->
      <div id="abstract-search-card" class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 hover:shadow-md transition-shadow">
        <!-- 頂部總覽標題與總篇數徽章 -->
        <div class="flex items-start space-x-3 mb-3.5">
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
              即時檢索口頭與海報發表論文。請直接在下方對應的「口頭發表」或「海報發表」專區輸入論文編號或報告者姓名查詢。
            </p>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 第一區：「1、口頭發表」獨立查詢專區 (Oral) -->
        <!-- ========================================== -->
        <div id="oral-search-section" class="p-3 bg-amber-50/40 rounded-2xl border border-amber-200/80 mb-4 shadow-2xs">
          <!-- 區塊標題列 -->
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-1.5">
              <i class="fa-solid fa-chalkboard-user text-amber-600 text-xs"></i>
              <h4 id="oral-section-title" class="text-xs font-black text-amber-950">1、口頭發表 (Oral)</h4>
              <span id="oral-total-badge" class="text-[10px] bg-amber-100 text-amber-900 font-bold px-1.5 py-0.2 rounded-full border border-amber-300">74 篇</span>
            </div>
            <span id="oral-hint-badge" class="text-[10px] text-amber-700 font-medium">完整 6 項資訊</span>
          </div>

          <!-- 獨立搜尋輸入列 + 查詢按鈕 -->
          <div class="flex items-center space-x-1.5 mb-2">
            <div class="relative flex-1 flex items-center">
              <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
              <input id="oral-search-input" type="text" oninput="handleOralSearchInput(this.value)" onkeydown="if(event.key==='Enter') executeOralSearch()" placeholder="輸入口頭論文編號或報告者..." class="w-full pl-8 pr-7 py-2 bg-white border border-slate-200 focus:border-amber-500 rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none transition-all font-medium">
              <button id="oral-clear-btn" onclick="clearOralSearch()" class="hidden absolute right-2.5 w-4 h-4 rounded-full bg-slate-300 text-white hover:bg-slate-400 flex items-center justify-center text-[9px]">
                <i class="fa-solid fa-xmark"></i>
              </button>
            </div>
            <button onclick="executeOralSearch()" id="oral-search-btn" class="px-3.5 py-2 bg-gradient-to-r from-amber-500 to-amber-400 hover:from-amber-600 hover:to-amber-500 text-slate-950 rounded-xl text-xs font-bold transition-all shadow-xs flex items-center space-x-1 shrink-0">
              <i class="fa-solid fa-magnifying-glass text-[11px]"></i>
              <span id="oral-search-btn-text">查詢</span>
            </button>
          </div>

          <!-- 結果計數 -->
          <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1.5 px-0.5">
            <span id="oral-results-count" class="font-bold text-amber-900">顯示 74 篇口頭發表</span>
          </div>

          <!-- 獨立結果滾動列表 (max-h-64) -->
          <div id="oral-results-list" class="space-y-2.5 max-h-64 overflow-y-auto no-scrollbar pr-0.5">
            <!-- Rendered dynamically by JavaScript -->
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 第二區：「2、海報發表」獨立查詢專區 (Poster) -->
        <!-- ========================================== -->
        <div id="poster-search-section" class="p-3 bg-cyan-50/40 rounded-2xl border border-cyan-200/80 shadow-2xs">
          <!-- 區塊標題列 -->
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-1.5">
              <i class="fa-solid fa-image text-cyan-600 text-xs"></i>
              <h4 id="poster-section-title" class="text-xs font-black text-cyan-950">2、海報發表 (Poster)</h4>
              <span id="poster-total-badge" class="text-[10px] bg-cyan-100 text-cyan-900 font-bold px-1.5 py-0.2 rounded-full border border-cyan-300">143 篇</span>
            </div>
            <span id="poster-hint-badge" class="text-[10px] text-cyan-800 font-medium">1F 海報展區 12:30-13:30 交流</span>
          </div>

          <!-- 獨立搜尋輸入列 + 查詢按鈕 -->
          <div class="flex items-center space-x-1.5 mb-2">
            <div class="relative flex-1 flex items-center">
              <i class="fa-solid fa-magnifying-glass absolute left-3 text-slate-400 text-xs"></i>
              <input id="poster-search-input" type="text" oninput="handlePosterSearchInput(this.value)" onkeydown="if(event.key==='Enter') executePosterSearch()" placeholder="輸入海報論文編號或報告者..." class="w-full pl-8 pr-7 py-2 bg-white border border-slate-200 focus:border-cyan-500 rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none transition-all font-medium">
              <button id="poster-clear-btn" onclick="clearPosterSearch()" class="hidden absolute right-2.5 w-4 h-4 rounded-full bg-slate-300 text-white hover:bg-slate-400 flex items-center justify-center text-[9px]">
                <i class="fa-solid fa-xmark"></i>
              </button>
            </div>
            <button onclick="executePosterSearch()" id="poster-search-btn" class="px-3.5 py-2 bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-700 hover:to-cyan-600 text-white rounded-xl text-xs font-bold transition-all shadow-xs flex items-center space-x-1 shrink-0">
              <i class="fa-solid fa-magnifying-glass text-[11px]"></i>
              <span id="poster-search-btn-text">查詢</span>
            </button>
          </div>

          <!-- 結果計數 -->
          <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1.5 px-0.5">
            <span id="poster-results-count" class="font-bold text-cyan-900">顯示 143 篇海報發表</span>
          </div>

          <!-- 獨立結果滾動列表 (max-h-64) -->
          <div id="poster-results-list" class="space-y-2 max-h-64 overflow-y-auto no-scrollbar pr-0.5">
            <!-- Rendered dynamically by JavaScript -->
          </div>
        </div>
      </div>

      '''

html = html[:idx_html_start] + new_card4_html + html[idx_html_end:]
print("Part 1 SUCCESS: Card 4 HTML replaced with dual independent search zones.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
