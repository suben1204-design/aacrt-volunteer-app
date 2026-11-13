# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx1 = html.find('function askAiAboutPaper')
idx_start = html.rfind('    // ==========================================\n    // 論文摘要即時檢索卡邏輯', 0, idx1)
assert idx1 != -1 and idx_start != -1

new_js = """    // ==========================================
    // 論文摘要即時檢索 (Abstracts Search: Oral vs Poster)
    // ==========================================
    let ABSTRACTS_DATA = [];
    let ORAL_PAPERS = [];
    let POSTER_PAPERS = [];
    let currentAbstractTab = 'oral'; // 'oral' | 'poster'
    let oralSearchQuery = '';
    let posterSearchQuery = '';

    async function loadAbstractsIndex() {
      try {
        const resp = await fetch('./docs/abstracts_index.json');
        if (!resp.ok) throw new Error('HTTP ' + resp.status);
        const data = await resp.json();
        ABSTRACTS_DATA = Array.isArray(data) ? data : (data.papers || data.abstracts || []);
        
        // 分流：口頭 vs 海報
        ORAL_PAPERS = ABSTRACTS_DATA.filter(p => {
          const t = (p.type || '').toLowerCase();
          return t.includes('oral') || t.includes('口頭') || (p.id || '').toUpperCase().startsWith('O-');
        });
        POSTER_PAPERS = ABSTRACTS_DATA.filter(p => {
          const t = (p.type || '').toLowerCase();
          return t.includes('poster') || t.includes('海報') || t.includes('壁報') || (p.id || '').toUpperCase().startsWith('P-');
        });

        console.log(`✅ Loaded abstracts: Total ${ABSTRACTS_DATA.length} (Oral: ${ORAL_PAPERS.length}, Poster: ${POSTER_PAPERS.length})`);
        
        // 更新徽章數字與渲染清單
        updateAbstractBadges();
        renderOralResults();
        renderPosterResults();
      } catch (err) {
        console.warn('Could not load abstracts_index.json:', err);
        const countBadge = document.getElementById('abstract-indexed-badge');
        if (countBadge) {
          countBadge.innerText = (currentLang === 'zh-TW') ? '論文索引加載中' : 'Index loading...';
        }
      }
    }

    function updateAbstractBadges() {
      const countBadge = document.getElementById('abstract-indexed-badge');
      if (countBadge) {
        const badgeText = (currentLang === 'zh-TW') ? `${ABSTRACTS_DATA.length} 篇論文已索引` :
                          (currentLang === 'ja') ? `${ABSTRACTS_DATA.length}件の論文索引完了` :
                          (currentLang === 'ko') ? `${ABSTRACTS_DATA.length}편 논문 색인 완료` :
                          `${ABSTRACTS_DATA.length} Papers Indexed`;
        countBadge.innerText = badgeText;
      }
      const oralBadge = document.getElementById('abs-oral-badge');
      if (oralBadge) oralBadge.innerText = ORAL_PAPERS.length;
      const posterBadge = document.getElementById('abs-poster-badge');
      if (posterBadge) posterBadge.innerText = POSTER_PAPERS.length;
    }

    function switchAbstractTab(tab) {
      currentAbstractTab = tab;
      const tabOral = document.getElementById('abs-tab-oral');
      const tabPoster = document.getElementById('abs-tab-poster');
      const panelOral = document.getElementById('abs-oral-panel');
      const panelPoster = document.getElementById('abs-poster-panel');

      if (tab === 'oral') {
        tabOral.className = 'flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 shadow-sm bg-white text-cyan-900 border border-slate-200';
        tabPoster.className = 'flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 text-slate-600 hover:text-slate-900';
        panelOral.classList.remove('hidden');
        panelPoster.classList.add('hidden');
      } else {
        tabPoster.className = 'flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 shadow-sm bg-white text-cyan-900 border border-slate-200';
        tabOral.className = 'flex-1 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center justify-center space-x-1.5 text-slate-600 hover:text-slate-900';
        panelPoster.classList.remove('hidden');
        panelOral.classList.add('hidden');
      }
    }

    // 口頭發表搜尋
    function handleOralSearch(query) {
      oralSearchQuery = (query || '').trim();
      const clearBtn = document.getElementById('abstract-oral-clear-btn');
      if (clearBtn) {
        if (oralSearchQuery.length > 0) clearBtn.classList.remove('hidden');
        else clearBtn.classList.add('hidden');
      }
      renderOralResults();
    }

    function clearOralSearch() {
      const input = document.getElementById('abstract-oral-search-input');
      if (input) input.value = '';
      oralSearchQuery = '';
      const clearBtn = document.getElementById('abstract-oral-clear-btn');
      if (clearBtn) clearBtn.classList.add('hidden');
      renderOralResults();
    }

    // 海報發表搜尋
    function handlePosterSearch(query) {
      posterSearchQuery = (query || '').trim();
      const clearBtn = document.getElementById('abstract-poster-clear-btn');
      if (clearBtn) {
        if (posterSearchQuery.length > 0) clearBtn.classList.remove('hidden');
        else clearBtn.classList.add('hidden');
      }
      renderPosterResults();
    }

    function clearPosterSearch() {
      const input = document.getElementById('abstract-poster-search-input');
      if (input) input.value = '';
      posterSearchQuery = '';
      const clearBtn = document.getElementById('abstract-poster-clear-btn');
      if (clearBtn) clearBtn.classList.add('hidden');
      renderPosterResults();
    }

    // 渲染「1、口頭發表」清單 (呈現 6 項核心資訊)
    function renderOralResults() {
      const container = document.getElementById('abstract-oral-list');
      const counterEl = document.getElementById('abstract-oral-count');
      if (!container) return;

      if (!ORAL_PAPERS || ORAL_PAPERS.length === 0) {
        container.innerHTML = `
          <div class="py-8 text-center text-slate-400 bg-slate-50 rounded-xl border border-dashed border-slate-200">
            <i class="fa-solid fa-file-excel text-2xl mb-1.5 text-amber-500"></i>
            <p class="text-xs font-bold text-slate-700">等待上傳口頭發表資料 (Google Sheets / Excel)</p>
            <p class="text-[11px] text-slate-400 mt-0.5">待資料上傳後即刻同步啟用檢索</p>
          </div>
        `;
        if (counterEl) counterEl.innerText = '等待資料上傳 (0 篇)';
        return;
      }

      const q = oralSearchQuery.toLowerCase();
      const filtered = ORAL_PAPERS.filter(item => {
        if (!q) return true;
        const idMatch = (item.id || '').toLowerCase().includes(q);
        const speakerMatch = (item.speaker || '').toLowerCase().includes(q);
        return idMatch || speakerMatch;
      });

      if (counterEl) {
        const countText = (currentLang === 'zh-TW') ? `顯示 ${filtered.length} 篇口頭發表 (共 ${ORAL_PAPERS.length} 篇)` :
                          (currentLang === 'ja') ? `${filtered.length} 件の口頭発表を表示 (全 ${ORAL_PAPERS.length} 件)` :
                          (currentLang === 'ko') ? `${filtered.length} 편 구연 발표 표시 (총 ${ORAL_PAPERS.length} 편)` :
                          `Showing ${filtered.length} of ${ORAL_PAPERS.length} Oral Presentations`;
        counterEl.innerText = countText;
      }

      if (filtered.length === 0) {
        const noResultMsg = (currentLang === 'zh-TW') ? '查無符合條件的口頭發表論文，請嘗試其他編號或報告者姓名' :
                            (currentLang === 'ja') ? '該当する口頭発表が見つかりません。別の論文番号または発表者氏名をお試しください' :
                            (currentLang === 'ko') ? '일치하는 구연 발표가 없습니다. 다른 논문 번호 또는 발표자 이름을 입력해 주세요' :
                            'No matching oral presentations found. Please try another paper ID or presenter name.';
        container.innerHTML = `
          <div class="py-6 text-center text-slate-400 bg-slate-50 rounded-xl border border-dashed border-slate-200">
            <i class="fa-solid fa-magnifying-glass text-xl mb-1 text-slate-300"></i>
            <p class="text-xs">${noResultMsg}</p>
          </div>
        `;
        return;
      }

      const displayList = filtered.slice(0, 60);
      const labels = getFieldLabels();

      container.innerHTML = displayList.map(item => {
        const cleanId = escapeHtml(item.id || '');
        const cleanTitle = escapeHtml(item.title || '');
        const cleanSpeaker = escapeHtml(item.speaker || '');
        const cleanRoom = escapeHtml(item.room || '');
        const cleanTime = escapeHtml(item.time || '');
        const cleanChairs = escapeHtml(item.chairs || '大會座長');
        const cleanCat = escapeHtml(item.category || '');

        return `
          <div class="p-3 bg-slate-50 hover:bg-amber-50/40 rounded-xl border border-slate-200 transition-all flex flex-col justify-between shadow-xs">
            <div>
              <!-- 頂部：論文編號 + 琥珀色口頭標籤 + 發表時間 -->
              <div class="flex items-center justify-between gap-1.5 mb-1.5">
                <div class="flex items-center space-x-1.5">
                  <span class="text-[10px] font-mono font-black text-amber-900 bg-amber-100/90 px-2 py-0.5 rounded border border-amber-300">
                    <span class="text-[9px] text-amber-700 mr-0.5">${labels.paperId}:</span>${cleanId}
                  </span>
                  <span class="text-[9px] font-bold bg-amber-500 text-slate-950 px-1.5 py-0.5 rounded shadow-xs">口頭</span>
                </div>
                <span class="text-[10px] font-mono font-bold text-slate-600 bg-white px-2 py-0.5 rounded border border-slate-200 flex items-center gap-1">
                  <i class="fa-regular fa-clock text-amber-600 text-[10px]"></i>${cleanTime}
                </span>
              </div>

              <!-- 發表題目 -->
              <h4 class="text-xs font-extrabold text-slate-900 leading-snug mb-2" title="${cleanTitle}">
                ${cleanTitle}
              </h4>

              <!-- 6 大詳細資訊網格 (會議室、座長、報告者) -->
              <div class="grid grid-cols-2 gap-1.5 text-[11px] bg-white p-2 rounded-lg border border-slate-200/80 mb-2">
                <div class="flex items-center space-x-1.5 truncate">
                  <i class="fa-solid fa-door-open text-amber-600 text-xs shrink-0"></i>
                  <span class="text-slate-400 text-[10px] shrink-0">${labels.room}:</span>
                  <span class="font-bold text-slate-800 truncate">${cleanRoom}</span>
                </div>
                <div class="flex items-center space-x-1.5 truncate">
                  <i class="fa-solid fa-user text-amber-600 text-xs shrink-0"></i>
                  <span class="text-slate-400 text-[10px] shrink-0">${labels.speaker}:</span>
                  <span class="font-bold text-slate-800 truncate">${cleanSpeaker}</span>
                </div>
                <div class="col-span-2 flex items-center space-x-1.5 truncate pt-1 border-t border-slate-100">
                  <i class="fa-solid fa-user-tie text-slate-400 text-xs shrink-0"></i>
                  <span class="text-slate-400 text-[10px] shrink-0">${labels.chairs}:</span>
                  <span class="text-slate-700 truncate font-medium">${cleanChairs}</span>
                </div>
              </div>
            </div>

            <!-- 底部動作按鈕 (問 AI + 秀給外賓) -->
            <div class="flex items-center justify-end space-x-1.5 pt-1 border-t border-slate-200/60">
              <button onclick="askAiAboutPaper('${cleanId}', '${cleanTitle.replace(/'/g, "\\'")}')" class="px-2.5 py-1 rounded-lg bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 text-[10px] font-bold transition-all shadow-xs flex items-center space-x-1">
                <i class="fa-solid fa-sparkles text-amber-500"></i>
                <span>${labels.askAi}</span>
              </button>
              <button onclick="showAbstractToGuest('${cleanId}', '${cleanTitle.replace(/'/g, "\\'")}', '${cleanCat}', 'Oral (口頭)', '${cleanSpeaker}', '${cleanRoom}', '${cleanTime}')" class="px-2.5 py-1 rounded-lg bg-gradient-to-r from-amber-500 to-amber-400 hover:from-amber-600 hover:to-amber-500 text-slate-950 text-[10px] font-bold transition-all shadow-xs flex items-center space-x-1">
                <i class="fa-solid fa-mobile-screen"></i>
                <span>${labels.showGuest}</span>
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    // 渲染「2、海報發表」清單 (簡潔呈現 2 項規格資料：論文編號 + 報告者)
    function renderPosterResults() {
      const container = document.getElementById('abstract-poster-list');
      const counterEl = document.getElementById('abstract-poster-count');
      if (!container) return;

      if (!POSTER_PAPERS || POSTER_PAPERS.length === 0) {
        container.innerHTML = `
          <div class="py-8 text-center text-slate-400 bg-slate-50 rounded-xl border border-dashed border-slate-200">
            <i class="fa-solid fa-file-excel text-2xl mb-1.5 text-cyan-600"></i>
            <p class="text-xs font-bold text-slate-700">等待上傳海報發表資料 (Google Sheets / Excel)</p>
            <p class="text-[11px] text-slate-400 mt-0.5">待資料上傳後即刻同步啟用檢索</p>
          </div>
        `;
        if (counterEl) counterEl.innerText = '等待資料上傳 (0 篇)';
        return;
      }

      const q = posterSearchQuery.toLowerCase();
      const filtered = POSTER_PAPERS.filter(item => {
        if (!q) return true;
        const idMatch = (item.id || '').toLowerCase().includes(q);
        const speakerMatch = (item.speaker || '').toLowerCase().includes(q);
        return idMatch || speakerMatch;
      });

      if (counterEl) {
        const countText = (currentLang === 'zh-TW') ? `顯示 ${filtered.length} 篇海報發表 (共 ${POSTER_PAPERS.length} 篇)` :
                          (currentLang === 'ja') ? `${filtered.length} 件のポスター発表を表示 (全 ${POSTER_PAPERS.length} 件)` :
                          (currentLang === 'ko') ? `${filtered.length} 편 포스터 발표 표시 (총 ${POSTER_PAPERS.length} 편)` :
                          `Showing ${filtered.length} of ${POSTER_PAPERS.length} Poster Presentations`;
        counterEl.innerText = countText;
      }

      if (filtered.length === 0) {
        const noResultMsg = (currentLang === 'zh-TW') ? '查無符合條件的海報發表論文，請嘗試其他編號或報告者姓名' :
                            (currentLang === 'ja') ? '該当するポスター発表が見つかりません。別の論文番号または発表者氏名をお試しください' :
                            (currentLang === 'ko') ? '일치하는 포스터 발표가 없습니다. 다른 논문 번호 또는 발표자 이름을 입력해 주세요' :
                            'No matching poster presentations found. Please try another paper ID or presenter name.';
        container.innerHTML = `
          <div class="py-6 text-center text-slate-400 bg-slate-50 rounded-xl border border-dashed border-slate-200">
            <i class="fa-solid fa-magnifying-glass text-xl mb-1 text-slate-300"></i>
            <p class="text-xs">${noResultMsg}</p>
          </div>
        `;
        return;
      }

      const displayList = filtered.slice(0, 60);
      const labels = getFieldLabels();

      container.innerHTML = displayList.map(item => {
        const cleanId = escapeHtml(item.id || '');
        const cleanTitle = escapeHtml(item.title || '');
        const cleanSpeaker = escapeHtml(item.speaker || '');
        const cleanCat = escapeHtml(item.category || '');

        return `
          <div class="p-2.5 bg-slate-50 hover:bg-cyan-50/40 rounded-xl border border-slate-200 transition-all flex items-center justify-between shadow-xs">
            <!-- 左側：簡潔呈現 2 項規格資料 (論文編號 + 報告者) -->
            <div class="flex items-center space-x-2.5 min-w-0 pr-2">
              <span class="text-[11px] font-mono font-black text-cyan-900 bg-cyan-100/90 px-2 py-0.5 rounded border border-cyan-300 shrink-0">
                <span class="text-[9px] text-cyan-700 mr-0.5">${labels.paperId}:</span>${cleanId}
              </span>
              <div class="flex items-center space-x-1.5 truncate">
                <i class="fa-solid fa-user text-cyan-700 text-xs shrink-0"></i>
                <span class="text-slate-400 text-[10px] shrink-0">${labels.speaker}:</span>
                <span class="font-extrabold text-slate-900 text-xs truncate">${cleanSpeaker}</span>
              </div>
            </div>

            <!-- 右側：動作按鈕 (問 AI + 秀給外賓) -->
            <div class="flex items-center space-x-1 shrink-0">
              <button onclick="askAiAboutPaper('${cleanId}', '${cleanTitle.replace(/'/g, "\\'")}')" class="px-2 py-1 rounded bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 text-[10px] font-bold transition-all shadow-xs">
                <i class="fa-solid fa-sparkles text-amber-500 mr-0.5"></i>${labels.askAi}
              </button>
              <button onclick="showAbstractToGuest('${cleanId}', '${cleanTitle.replace(/'/g, "\\'")}', '${cleanCat}', 'Poster (海報)', '${cleanSpeaker}', '1F 海報展區', '12:30-13:30')" class="px-2 py-1 rounded bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-700 hover:to-cyan-600 text-white text-[10px] font-bold transition-all shadow-xs">
                <i class="fa-solid fa-mobile-screen mr-0.5"></i>${labels.showGuest}
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    function getFieldLabels() {
      if (currentLang === 'ja') {
        return {
          room: '会場',
          chairs: '座長',
          paperId: '論文番号',
          speaker: '発表者',
          time: '発表時間',
          title: '演題名',
          askAi: 'AI質問',
          showGuest: '外賓提示'
        };
      } else if (currentLang === 'ko') {
        return {
          room: '회의실',
          chairs: '좌장',
          paperId: '논문번호',
          speaker: '발표자',
          time: '발표시간',
          title: '발표제목',
          askAi: 'AI질문',
          showGuest: '게스트보기'
        };
      } else if (currentLang === 'en') {
        return {
          room: 'Room',
          chairs: 'Chairs',
          paperId: 'Paper ID',
          speaker: 'Presenter',
          time: 'Time',
          title: 'Title',
          askAi: 'Ask AI',
          showGuest: 'Show Guest'
        };
      } else {
        return {
          room: '會議室',
          chairs: '座長',
          paperId: '論文編號',
          speaker: '報告者',
          time: '發表時間',
          title: '發表題目',
          askAi: '問 AI',
          showGuest: '秀給外賓'
        };
      }
    }

    """

html = html[:idx_start] + new_js + html[idx1:]
print("Step 2 SUCCESS: JS logic successfully replaced.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
