import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 替換 HTML 標籤按鈕
old_pills = """          <button onclick="filterAbstractCategory('ALL')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-800 text-cyan-300 shrink-0 shadow-sm transition-all" data-cat="ALL">全部 (0)</button>
          <button onclick="filterAbstractCategory('AI')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="AI">AI 人工智慧 (0)</button>
          <button onclick="filterAbstractCategory('CT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="CT">CT 電腦斷層 (0)</button>
          <button onclick="filterAbstractCategory('MR')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="MR">MRI 磁振造影 (0)</button>
          <button onclick="filterAbstractCategory('RT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="RT">RT 放射治療 (0)</button>
          <button onclick="filterAbstractCategory('NM')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="NM">NM 核子醫學 (0)</button>
          <button onclick="filterAbstractCategory('CA')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="CA">CA 心導管 (0)</button>
          <button onclick="filterAbstractCategory('IR')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="IR">IR 血管介入 (0)</button>
          <button onclick="filterAbstractCategory('MA')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="MA">MA 乳房攝影 (0)</button>
          <button onclick="filterAbstractCategory('RO')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="RO">RO 常規X光 (0)</button>
          <button onclick="filterAbstractCategory('ST')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="ST">ST 學生研究 (0)</button>
          <button onclick="filterAbstractCategory('OT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="OT">OT 綜合其他 (0)</button>"""

new_pills = """          <button onclick="filterAbstractCategory('ALL')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-800 text-cyan-300 shrink-0 shadow-sm transition-all" data-cat="ALL">全部 (217)</button>
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
          <button onclick="filterAbstractCategory('OT')" class="abs-cat-btn px-2.5 py-1 rounded-lg font-bold bg-slate-100 text-slate-600 hover:text-slate-900 shrink-0 transition-all" data-cat="OT">OT 綜合其他 (41)</button>"""

# 2. 替換 catLabels
old_labels = """      const catLabels = {
        'zh-TW': { ALL: '全部 (0)', AI: 'AI 人工智慧 (0)', CT: 'CT 電腦斷層 (0)', MR: 'MRI 磁振造影 (0)', RT: 'RT 放射治療 (0)', NM: 'NM 核子醫學 (0)', CA: 'CA 心導管 (0)', IR: 'IR 血管介入 (0)', MA: 'MA 乳房攝影 (0)', RO: 'RO 常規X光 (0)', ST: 'ST 學生研究 (0)', OT: 'OT 綜合其他 (0)' },
        'en':    { ALL: 'ALL (0)', AI: 'AI (0)', CT: 'CT (0)', MR: 'MRI (0)', RT: 'RT (0)', NM: 'NM (0)', CA: 'Cath Lab (0)', IR: 'Interventional (0)', MA: 'Mammography (0)', RO: 'Radiography (0)', ST: 'Student (0)', OT: 'Other (0)' },
        'ja':    { ALL: '全て (0)', AI: 'AI (0)', CT: 'CT (0)', MR: 'MRI (0)', RT: '放射線治療 (0)', NM: '核医学 (0)', CA: '心カテ (0)', IR: '血管造影 (0)', MA: 'マンモ (0)', RO: '一般X線 (0)', ST: '学生研究 (0)', OT: 'その他 (0)' },
        'ko':    { ALL: '전체 (0)', AI: 'AI (0)', CT: 'CT (0)', MR: 'MRI (0)', RT: '방사선치료 (0)', NM: '핵의학 (0)', CA: '심도자 (0)', IR: '인터벤션 (0)', MA: '유방촬영 (0)', RO: '일반촬영 (0)', ST: '학생연구 (0)', OT: '기타 (0)' }
      };"""

new_labels = """      const catLabels = {
        'zh-TW': { ALL: '全部 (217)', AI: 'AI 人工智慧 (14)', CT: 'CT 電腦斷層 (16)', MR: 'MRI 磁振造影 (21)', RT: 'RT 放射治療 (23)', NM: 'NM 核子醫學 (8)', CA: 'CA 心導管 (11)', IR: 'IR 血管介入 (7)', MA: 'MA 乳房攝影 (7)', RO: 'RO 常規X光 (12)', US: 'US 超音波 (2)', ST: 'ST 學生研究 (55)', OT: 'OT 綜合其他 (41)' },
        'en':    { ALL: 'ALL (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: 'RT (23)', NM: 'NM (8)', CA: 'Cath Lab (11)', IR: 'Interventional (7)', MA: 'Mammography (7)', RO: 'Radiography (12)', US: 'Ultrasound (2)', ST: 'Student (55)', OT: 'Other (41)' },
        'ja':    { ALL: '全て (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: '放射線治療 (23)', NM: '核医学 (8)', CA: '心カテ (11)', IR: '血管造影 (7)', MA: 'マンモ (7)', RO: '一般X線 (12)', US: '超音波 (2)', ST: '学生研究 (55)', OT: 'その他 (41)' },
        'ko':    { ALL: '전체 (217)', AI: 'AI (14)', CT: 'CT (16)', MR: 'MRI (21)', RT: '방사선치료 (23)', NM: '핵의학 (8)', CA: '심도자 (11)', IR: '인터벤션 (7)', MA: '유방촬영 (7)', RO: '일반촬영 (12)', US: '초음파 (2)', ST: '학생연구 (55)', OT: '기타 (41)' }
      };"""

assert old_pills in content, 'old_pills not found'
assert old_labels in content, 'old_labels not found'

content = content.replace(old_pills, new_pills)
content = content.replace(old_labels, new_labels)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS: updated index.html with 217 counts and US category!')
