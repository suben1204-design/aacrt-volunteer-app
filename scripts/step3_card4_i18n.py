# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 3. 替換 i18n 字典中的 abstract 欄位與 updateLanguageUI
# ---------------------------------------------------------------------------

# 3.1 zh-TW 字典替換
old_zh = """          abstractCardTitle: '4、學術論文摘要即時檢索 (Abstract Search)',
          abstractCardDesc: '即時檢索口頭與壁報論文。支援專題領域（CT、MRI、AI、放療等）、論文編號（如 P-CT-008、O-AI-001）或關鍵字。',
          abstractPlaceholder: '輸入論文編號、題目或關鍵字 (如 CT, AI, PSMA, 劑量)...',
          abstractCatAll: '全部'
        },"""

new_zh = """          abstractCardTitle: '4、學術論文摘要即時檢索 (Abstract Search)',
          abstractCardDesc: '即時檢索口頭與海報發表論文。請切換下方分頁，輸入「論文編號」或「報告者姓名」進行精準篩選。',
          absTabOral: '1、口頭發表 (Oral)',
          absTabPoster: '2、海報發表 (Poster)',
          absOralSearchPlaceholder: '輸入論文編號或報告者姓名 (如 O-NMR-01, 陳大同)...',
          absPosterSearchPlaceholder: '輸入論文編號或報告者姓名 (如 P-AI-001, 吳怡萱)...',
          absOralHint: '完整列出 6 項發表資訊',
          absPosterHint: '展區：1F 海報展區 (12:30-13:30 交流)'
        },"""

# 3.2 en 字典替換
old_en = """          abstractCardTitle: '4. Scientific Abstracts Search',
          abstractCardDesc: 'Instant search across oral and poster abstracts by track (CT, MRI, AI, RT), paper ID (e.g. P-CT-008, O-AI-001) or keywords.',
          abstractPlaceholder: 'Search by paper ID, title or keyword (e.g. CT, AI, dose)...',
          abstractCatAll: 'ALL'
        },"""

new_en = """          abstractCardTitle: '4. Scientific Abstracts Search',
          abstractCardDesc: 'Instant search for Oral and Poster presentations. Switch tabs below and filter by Paper ID or Presenter Name.',
          absTabOral: '1. Oral Presentation',
          absTabPoster: '2. Poster Presentation',
          absOralSearchPlaceholder: 'Enter Paper ID or Presenter (e.g. O-NMR-01, John Doe)...',
          absPosterSearchPlaceholder: 'Enter Paper ID or Presenter (e.g. P-AI-001, Jane Smith)...',
          absOralHint: 'Complete 6 presentation fields listed',
          absPosterHint: 'Exhibition: 1F Poster Area (12:30-13:30)'
        },"""

# 3.3 ja 字典替換
old_ja = """          abstractCardTitle: '4. 学術論文抄録即時検索 (Abstract Search)',
          abstractCardDesc: '口頭発表・ポスター抄録を専門分野（CT、MRI、AI、放射線治療など）、論文番号（例：P-CT-008、O-AI-001）やキーワードで即時検索。',
          abstractPlaceholder: '論文番号、タイトル、キーワードを入力 (例: CT, AI, 線量)...',
          abstractCatAll: '全て'
        },"""

new_ja = """          abstractCardTitle: '4. 学術論文抄録即時検索 (Abstract Search)',
          abstractCardDesc: '口頭発表およびポスター発表の即時検索。タブを切り替え、「論文番号」または「発表者氏名」を入力して検索してください。',
          absTabOral: '1. 口頭発表 (Oral)',
          absTabPoster: '2. ポスター発表 (Poster)',
          absOralSearchPlaceholder: '論文番号または発表者氏名を入力 (例: O-NMR-01, 田中)...',
          absPosterSearchPlaceholder: '論文番号または発表者氏名を入力 (例: P-AI-001, 佐藤)...',
          absOralHint: '発表に関する6項目を完全表示',
          absPosterHint: '会場：1F ポスター会場 (12:30-13:30 質疑)'
        },"""

# 3.4 ko 字典替換
old_ko = """          abstractCardTitle: '4. 학술대회 논문 초록 즉시 검색 (Abstract Search)',
          abstractCardDesc: '구연 및 포스터 초록을 전공 분야(CT, MRI, AI, 방사선치료 등), 논문 번호(예: P-CT-008, O-AI-001) 또는 키워드로 즉시 검색.',
          abstractPlaceholder: '논문 번호, 제목, 키워드 입력 (예: CT, AI, 선량)...',
          abstractCatAll: '전체'
        }"""

new_ko = """          abstractCardTitle: '4. 학술대회 논문 초록 즉시 검색 (Abstract Search)',
          abstractCardDesc: '구연 및 포스터 발표 논문 즉시 검색. 아래 탭을 전환한 후 「논문 번호」 또는 「발표자 이름」을 입력하여 검색하세요.',
          absTabOral: '1. 구연 발표 (Oral)',
          absTabPoster: '2. 포스터 발표 (Poster)',
          absOralSearchPlaceholder: '논문 번호 또는 발표자 이름 입력 (예: O-NMR-01, 김철수)...',
          absPosterSearchPlaceholder: '논문 번호 또는 발표자 이름 입력 (예: P-AI-001, 이영희)...',
          absOralHint: '발표 관련 6개 항목 상세 표시',
          absPosterHint: '전시장: 1F 포스터 발표장 (12:30-13:30)'
        }"""

assert old_zh in html, "old_zh not found"
assert old_en in html, "old_en not found"
assert old_ja in html, "old_ja not found"
assert old_ko in html, "old_ko not found"

html = html.replace(old_zh, new_zh)
html = html.replace(old_en, new_en)
html = html.replace(old_ja, new_ja)
html = html.replace(old_ko, new_ko)

# 3.5 updateLanguageUI DOM 操作替換
old_dom_update = """      // Update Abstract Card i18n
      const abstractCardTitle = document.getElementById('abstract-card-title');
      if (abstractCardTitle) abstractCardTitle.innerText = t.abstractCardTitle;
      const abstractCardDesc = document.getElementById('abstract-card-desc');
      if (abstractCardDesc) abstractCardDesc.innerText = t.abstractCardDesc;
      const abstractInput = document.getElementById('abstract-search-input');
      if (abstractInput) abstractInput.placeholder = t.abstractPlaceholder;
      
      // Update Category Pills Language Labels
      const catLabels = {
        'zh-TW': { ALL: '全部 (217)', AI: 'AI 人工智慧 (14)', CT: 'CT 電腦斷層 (16)', MR: 'MRI 磁振造影 (21)', RT: 'RT 放射治療 (23)', NM: 'NM 核子醫學 (8)', CA: 'CA 心導管 (11)', IR: 'IR 血管介入 (7)', MA: 'MA 乳房攝影 (7)', RO: 'RO 常規X光 (12)', US: 'US 超音波 (2)', ST: 'ST 學生研究 (55)', OT: 'OT 綜合其他 (41)' },
        'en':    { ALL: 'ALL (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: 'RT (23)', NM: 'NM (8)', CA: 'Cath Lab (11)', IR: 'Interventional (7)', MA: 'Mammography (7)', RO: 'Radiography (12)', US: 'Ultrasound (2)', ST: 'Student (55)', OT: 'Other (41)' },
        'ja':    { ALL: '全て (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: '放射線治療 (23)', NM: '核医学 (8)', CA: '心カテ (11)', IR: '血管造影 (7)', MA: 'マンモ (7)', RO: '一般X線 (12)', US: '超音波 (2)', ST: '学生研究 (55)', OT: 'その他 (41)' },
        'ko':    { ALL: '전체 (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: '방사선치료 (23)', NM: '핵의학 (8)', CA: '심도자 (11)', IR: '인터벤션 (7)', MA: '유방촬영 (7)', RO: '일반촬영 (12)', US: '초음파 (2)', ST: '학생연구 (55)', OT: '기타 (41)' }
      };
      const activeCatMap = catLabels[currentLang] || catLabels['en'];
      document.querySelectorAll('.abs-cat-btn').forEach(btn => {
        const cat = btn.dataset.cat;
        if (cat && activeCatMap[cat]) {
          btn.innerText = activeCatMap[cat];
        }
      });"""

new_dom_update = """      // Update Abstract Card i18n
      const abstractCardTitle = document.getElementById('abstract-card-title');
      if (abstractCardTitle) abstractCardTitle.innerText = t.abstractCardTitle;
      const abstractCardDesc = document.getElementById('abstract-card-desc');
      if (abstractCardDesc) abstractCardDesc.innerText = t.abstractCardDesc;

      const absTabOralLabel = document.getElementById('abs-tab-oral-label');
      if (absTabOralLabel) absTabOralLabel.innerText = t.absTabOral;
      const absTabPosterLabel = document.getElementById('abs-tab-poster-label');
      if (absTabPosterLabel) absTabPosterLabel.innerText = t.absTabPoster;

      const oralInput = document.getElementById('abstract-oral-search-input');
      if (oralInput) oralInput.placeholder = t.absOralSearchPlaceholder;
      const posterInput = document.getElementById('abstract-poster-search-input');
      if (posterInput) posterInput.placeholder = t.absPosterSearchPlaceholder;

      const oralHint = document.getElementById('abstract-oral-hint');
      if (oralHint) oralHint.innerText = t.absOralHint;
      const posterHint = document.getElementById('abstract-poster-hint');
      if (posterHint) posterHint.innerText = t.absPosterHint;

      // 重新渲染當前清單標籤文字
      if (typeof renderOralResults === 'function') renderOralResults();
      if (typeof renderPosterResults === 'function') renderPosterResults();
      if (typeof updateAbstractBadges === 'function') updateAbstractBadges();"""

assert old_dom_update in html, "old_dom_update not found"
html = html.replace(old_dom_update, new_dom_update)

print("Step 3 SUCCESS: i18n dictionaries and DOM updates replaced.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
