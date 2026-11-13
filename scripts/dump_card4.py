with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
idx_start = content.find('4、學術論文摘要即時檢索')
div_start = content.rfind('<div class="bg-white rounded-2xl border border-slate-200', 0, idx_start)
idx_end = content.find('<!-- 諮詢台聯絡卡片 -->')
print('div_start:', div_start, 'idx_end:', idx_end)
with open('card4_old.txt', 'w', encoding='utf-8') as out:
    out.write(content[div_start:idx_end])
print('Wrote card4_old.txt, length:', idx_end - div_start)
