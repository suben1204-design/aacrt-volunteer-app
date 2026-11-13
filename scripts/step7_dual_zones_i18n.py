# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 3. 替換 i18n 字典中的 abstract 欄位與 updateLanguageUI
# ---------------------------------------------------------------------------

# 3.1 zh-TW 字典替換
old_zh = """          abstractCardTitle: '4、學術論文摘要即時檢索 (Abstract Search)',
          abstractCardDesc: '即時檢索口頭與海報發表論文。請切換下方分頁，輸入「論文編號」或「報告者姓名」進行精準篩選。',
          absTabOral: '1、口頭發表 (Oral)',
          absTabPoster: '2、海報發表 (Poster)',
          absOralSearchPlaceholder: '輸入論文編號或報告者姓名 (如 O-NMR-01, 陳大同)...',
          absPosterSearchPlaceholder: '輸入論文編號或報告者姓名 (如 P-AI-001, 吳怡萱)...',
          absOralHint: '完整列出 6 項發表資訊',
          absPosterHint: '展區：1F 海報展區 (12:30-13:30 交流)'
        },"""

new_zh = """          abstractCardTitle: '4、學術論文摘要即時檢索 (Abstract Search)',
          abstractCardDesc: '即時檢索口頭與海報發表論文。請直接在下方對應的「口頭發表」或「海報發表」專區輸入論文編號或報告者姓名查詢。',
          oralSectionTitle: '1、口頭發表 (Oral)',
          posterSectionTitle: '2、海報發表 (Poster)',
          oralSearchPlaceholder: '輸入口頭論文編號或報告者...',
          posterSearchPlaceholder: '輸入海報論文編號或報告者...',
          searchBtnText: '查詢',
          oralHint: '完整 6 項資訊',
          posterHint: '1F 海報展區 12:30-13:30 交流'
        },"""

# 3.2 en 字典替換
old_en = """          abstractCardTitle: '4. Scientific Abstracts Search',
          abstractCardDesc: 'Instant search for Oral and Poster presentations. Switch tabs below and filter by Paper ID or Presenter Name.',
          absTabOral: '1. Oral Presentation',
          absTabPoster: '2. Poster Presentation',
          absOralSearchPlaceholder: 'Enter Paper ID or Presenter (e.g. O-NMR-01, John Doe)...',
          absPosterSearchPlaceholder: 'Enter Paper ID or Presenter (e.g. P-AI-001, Jane Smith)...',
          absOralHint: 'Complete 6 presentation fields listed',
          absPosterHint: 'Exhibition: 1F Poster Area (12:30-13:30)'
        },"""

new_en = """          abstractCardTitle: '4. Scientific Abstracts Search',
          abstractCardDesc: 'Instant search across oral and poster abstracts. Enter Paper ID or Presenter directly in the respective zones below.',
          oralSectionTitle: '1. Oral Presentation (Oral)',
          posterSectionTitle: '2. Poster Presentation (Poster)',
          oralSearchPlaceholder: 'Search oral by paper ID or presenter...',
          posterSearchPlaceholder: 'Search poster by paper ID or presenter...',
          searchBtnText: 'Search',
          oralHint: 'Complete 6 fields listed',
          posterHint: '1F Poster Area 12:30-13:30'
        },"""

# 3.3 ja 字典替換
old_ja = """          abstractCardTitle: '4. 学術論文抄録即時検索 (Abstract Search)',
          abstractCardDesc: '口頭発表およびポスター発表の即時検索。タブを切り替え、「論文番号」または「発表者氏名」を入力して検索してください。',
          absTabOral: '1. 口頭発表 (Oral)',
          absTabPoster: '2. ポスター発表 (Poster)',
          absOralSearchPlaceholder: '論文番号または発表者氏名を入力 (例: O-NMR-01, 田中)...',
          absPosterSearchPlaceholder: '論文番号または発表者氏名を入力 (例: P-AI-001, 佐藤)...',
          absOralHint: '発表に関する6項目を完全表示',
          absPosterHint: '会場：1F ポスター会場 (12:30-13:30 質疑)'
        },"""

new_ja = """          abstractCardTitle: '4. 学術論文抄録即時検索 (Abstract Search)',
          abstractCardDesc: '口頭発表およびポスター発表の即時検索。下の各専用ゾーンにて論文番号または発表者氏名を入力して検索してください。',
          oralSectionTitle: '1. 口頭発表 (Oral)',
          posterSectionTitle: '2. ポスター発表 (Poster)',
          oralSearchPlaceholder: '口頭論文番号または発表者を入力...',
          posterSearchPlaceholder: 'ポスター論文番号または発表者を入力...',
          searchBtnText: '検索',
          oralHint: '6項目を完全表示',
          posterHint: '1F ポスター会場 12:30-13:30 質疑'
        },"""

# 3.4 ko 字典替換
old_ko = """          abstractCardTitle: '4. 학술대회 논문 초록 즉시 검색 (Abstract Search)',
          abstractCardDesc: '구연 및 포스터 발표 논문 즉시 검색. 아래 탭을 전환한 후 「논문 번호」 또는 「발표자 이름」을 입력하여 검색하세요.',
          absTabOral: '1. 구연 발표 (Oral)',
          absTabPoster: '2. 포스터 발표 (Poster)',
          absOralSearchPlaceholder: '논문 번호 또는 발표자 이름 입력 (예: O-NMR-01, 김철수)...',
          absPosterSearchPlaceholder: '논문 번호 또는 발표자 이름 입력 (예: P-AI-001, 이영희)...',
          absOralHint: '발표 관련 6개 항목 상세 표시',
          absPosterHint: '전시장: 1F 포스터 발표장 (12:30-13:30)'
        }"""

new_ko = """          abstractCardTitle: '4. 학술대회 논문 초록 즉시 검색 (Abstract Search)',
          abstractCardDesc: '구연 및 포스터 발표 논문 즉시 검색. 아래 전용 구역에서 논문 번호 또는 발표자 이름을 입력하여 검색하세요.',
          oralSectionTitle: '1. 구연 발표 (Oral)',
          posterSectionTitle: '2. 포스터 발표 (Poster)',
          oralSearchPlaceholder: '구연 논문 번호 또는 발표자 입력...',
          posterSearchPlaceholder: '포스터 논문 번호 또는 발표자 입력...',
          searchBtnText: '검색',
          oralHint: '6개 항목 상세 표시',
          posterHint: '1F 포스터 발표장 12:30-13:30'
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

new_dom_update = """      // Update Abstract Card i18n (Dual Independent Zones)
      const abstractCardTitle = document.getElementById('abstract-card-title');
      if (abstractCardTitle) abstractCardTitle.innerText = t.abstractCardTitle;
      const abstractCardDesc = document.getElementById('abstract-card-desc');
      if (abstractCardDesc) abstractCardDesc.innerText = t.abstractCardDesc;

      const oralSectionTitle = document.getElementById('oral-section-title');
      if (oralSectionTitle) oralSectionTitle.innerText = t.oralSectionTitle;
      const posterSectionTitle = document.getElementById('poster-section-title');
      if (posterSectionTitle) posterSectionTitle.innerText = t.posterSectionTitle;

      const oralInput = document.getElementById('oral-search-input');
      if (oralInput) oralInput.placeholder = t.oralSearchPlaceholder;
      const posterInput = document.getElementById('poster-search-input');
      if (posterInput) posterInput.placeholder = t.posterSearchPlaceholder;

      const oralSearchBtnText = document.getElementById('oral-search-btn-text');
      if (oralSearchBtnText) oralSearchBtnText.innerText = t.searchBtnText;
      const posterSearchBtnText = document.getElementById('poster-search-btn-text');
      if (posterSearchBtnText) posterSearchBtnText.innerText = t.searchBtnText;

      const oralHintBadge = document.getElementById('oral-hint-badge');
      if (oralHintBadge) oralHintBadge.innerText = t.oralHint;
      const posterHintBadge = document.getElementById('poster-hint-badge');
      if (posterHintBadge) posterHintBadge.innerText = t.posterHint;

      // 重新渲染當前清單標籤文字與計數
      if (typeof renderOralResults === 'function') renderOralResults();
      if (typeof renderPosterResults === 'function') renderPosterResults();
      if (typeof updateAbstractBadges === 'function') updateAbstractBadges();"""

assert old_dom_update in html, "old_dom_update not found"
html = html.replace(old_dom_update, new_dom_update)

print("Part 3 SUCCESS: i18n dictionaries and DOM updates replaced.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
