# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. 替換 QUICK_PROMPTS_DATA 與 renderQuickPromptsUI
# ---------------------------------------------------------------------------
idx1 = html.find('const QUICK_PROMPTS_DATA = [')
idx2 = html.find('function updateLanguageUI()')
assert idx1 != -1 and idx2 != -1, "QUICK_PROMPTS_DATA block not found"

new_prompts_code = """const QUICK_PROMPTS_DATA = [
      {
        icon: '🌟',
        key: 'keynote',
        'zh-TW': { label: '今日重要大會演講', prompt: '今日重要大會演講有哪些？' },
        'en':    { label: 'Keynote Addresses', prompt: 'What are the keynote and plenary sessions today?' },
        'ja':    { label: '本日の基調講演', prompt: '本日の基調講演とプレナリーセッションは？' },
        'ko':    { label: '오늘의 주요 기조강연', prompt: '오늘 진행되는 주요 기조강연은 무엇인가요?' }
      },
      {
        icon: '🏢',
        key: 'rooms',
        'zh-TW': { label: '7樓演講廳位置', prompt: '7樓大會堂與各演講廳怎麼走？' },
        'en':    { label: '7F Session Halls', prompt: 'How to get to the 7F Plenary Hall and session rooms?' },
        'ja':    { label: '7階各会場案内', prompt: '7階のプレナリーホールと各会議室への行き方は？' },
        'ko':    { label: '7층 강연장 위치', prompt: '7층 플레너리 홀과 각 회의실은 어떻게 가나요?' }
      }
    ];

    let cachedCloudTopQueries = [];

    function renderQuickPromptsUI() {
      const container = document.getElementById('quick-prompts-container');
      if (!container) return;

      // 若雲端熱搜已有資料，優先使用 2 欄雲端熱搜渲染
      if (cachedCloudTopQueries && cachedCloudTopQueries.length > 0) {
        renderDynamicTopQueries(cachedCloudTopQueries);
        return;
      }

      // 否則渲染預設的 2 項熱門提問 (單排 2 欄)
      container.innerHTML = QUICK_PROMPTS_DATA.slice(0, 2).map(item => {
        const loc = item[currentLang] || item['en'];
        return `
          <button onclick="sendQuickPrompt('${loc.prompt.replace(/'/g, "\\'")}')" class="text-xs bg-white border border-slate-200 hover:border-amber-400 text-slate-800 p-2.5 rounded-xl hover:text-amber-700 transition-all shadow-xs font-semibold text-left flex items-center space-x-2 truncate">
            <span class="text-sm shrink-0">${item.icon}</span>
            <span class="truncate">${loc.label}</span>
          </button>
        `;
      }).join('');
    }

    """

html = html[:idx1] + new_prompts_code + html[idx2:]
print("Part 1: Replaced QUICK_PROMPTS_DATA and renderQuickPromptsUI.")

# ---------------------------------------------------------------------------
# 2. 替換 renderDynamicTopQueries
# ---------------------------------------------------------------------------
idx3 = html.find('function renderDynamicTopQueries')
idx4 = html.find('// Initialization', idx3)
assert idx3 != -1 and idx4 != -1, "renderDynamicTopQueries block not found"

new_dynamic_code = """function renderDynamicTopQueries(topQueries) {
      if (!topQueries || topQueries.length === 0) return;
      cachedCloudTopQueries = topQueries;
      window.isCloudTopQueriesActive = true;

      const container = document.getElementById('quick-prompts-container');
      const badge = document.getElementById('live-stat-badge');
      if (badge) {
        badge.innerText = '🔥 現場大會熱搜中';
        badge.className = 'text-[10px] bg-amber-100 text-amber-900 px-2 py-0.5 rounded-full font-bold border border-amber-300 animate-pulse';
      }

      if (!container) return;

      // 嚴格限制最多 2 項熱搜 (topQueries 前 2 名)
      const topTwo = topQueries.slice(0, 2);
      let buttonsHtml = '';

      // 第 1 格：最高熱搜
      if (topTwo.length >= 1) {
        const q1 = topTwo[0];
        const cleanQ1 = escapeHtml(q1.length > 14 ? q1.substring(0, 14) + '...' : q1);
        buttonsHtml += `
          <button onclick="sendQuickPrompt('${escapeHtml(q1).replace(/'/g, "\\'")}')" class="text-xs bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-300 text-amber-900 p-2.5 rounded-xl hover:bg-amber-100 transition-all shadow-xs font-bold text-left flex items-center space-x-1.5 truncate">
            <span class="shrink-0">🔥</span>
            <span class="truncate">${cleanQ1}</span>
          </button>
        `;
      }

      // 第 2 格：次高熱搜；若僅有 1 筆，則自動補上預設第 1 項問題
      if (topTwo.length >= 2) {
        const q2 = topTwo[1];
        const cleanQ2 = escapeHtml(q2.length > 14 ? q2.substring(0, 14) + '...' : q2);
        buttonsHtml += `
          <button onclick="sendQuickPrompt('${escapeHtml(q2).replace(/'/g, "\\'")}')" class="text-xs bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-300 text-amber-900 p-2.5 rounded-xl hover:bg-amber-100 transition-all shadow-xs font-bold text-left flex items-center space-x-1.5 truncate">
            <span class="shrink-0">🔥</span>
            <span class="truncate">${cleanQ2}</span>
          </button>
        `;
      } else {
        const fallback = QUICK_PROMPTS_DATA[0];
        const loc = fallback[currentLang] || fallback['en'];
        buttonsHtml += `
          <button onclick="sendQuickPrompt('${loc.prompt.replace(/'/g, "\\'")}')" class="text-xs bg-white border border-slate-200 hover:border-amber-400 text-slate-800 p-2.5 rounded-xl hover:text-amber-700 transition-all shadow-xs font-semibold text-left flex items-center space-x-2 truncate">
            <span class="text-sm shrink-0">${fallback.icon}</span>
            <span class="truncate">${loc.label}</span>
          </button>
        `;
      }

      // 直接覆蓋，保證固定 2 格且不往上堆疊
      container.innerHTML = buttonsHtml;
    }

    """

html = html[:idx3] + new_dynamic_code + html[idx4:]
print("Part 2: Replaced renderDynamicTopQueries.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS: index.html updated!")
