#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2027 AACRT 知識大腦 - 論文摘要檢索與提煉測試流水線 (Abstract Pipeline Test Benchmark)
測試樣本來源：第59次年會暨國際醫學影像學術研討會-論文集.pdf (2026年測試樣本)
注意：本檔案僅作為結構化抽取、全文檢索壓力測試與學術術語萃取之用，嚴格與 2027 AACRT 正式大腦隔離。
"""

import os
import sys
import json
import re
from pathlib import Path
import pypdf

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = PROJECT_ROOT / "創作庫-內部原創層" / "第59次年會暨國際醫學影像學術研討會-論文集.pdf"
BENCHMARK_JSON = PROJECT_ROOT / "知識庫-AI 提煉層" / "test_abstracts_benchmark.json"

CATEGORY_MAP = {
    'CT': '電腦斷層 (Computed Tomography)',
    'MR': '磁振造影 (Magnetic Resonance Imaging)',
    'AI': '人工智慧 (Artificial Intelligence)',
    'RT': '放射治療 (Radiation Therapy)',
    'RO': '常規X光 (Routine Radiography)',
    'NM': '核子醫學 (Nuclear Medicine)',
    'IR': '血管攝影介入 (Interventional Radiology)',
    'CA': '心臟導管 (Cardiac Catheterization)',
    'MA': '乳房攝影 (Mammography)',
    'US': '超音波 (Ultrasound)',
    'ST': '學生研究 (Radiology Student Research)',
    'RN': '放射護理 (Radiology Nursing)',
    'EBM': '實證醫學 (Evidence-Based Medicine)',
    'OT': '其他放射技術 (Other)'
}

def clean_category(code):
    c = code.upper()
    if c.startswith('N') and len(c) > 2:
        c = c[1:]
    return c

def parse_proceedings(pdf_file=PDF_PATH):
    if not pdf_file.exists():
        print(f"錯誤：找不到測試檔案 {pdf_file}")
        return []

    print(f"📖 正在解析論文集 PDF: {pdf_file.name} ({pdf_file.stat().st_size / 1024 / 1024:.1f} MB)...")
    reader = pypdf.PdfReader(str(pdf_file))
    total_pages = len(reader.pages)
    print(f"📄 總頁數: {total_pages} 頁")

    pattern = re.compile(r'\b([OP])-([A-Z]{2,4})-(\d{1,4})\b')
    extracted = []

    for page_idx in range(total_pages):
        page = reader.pages[page_idx]
        text = page.extract_text() or ''
        lines = [l.strip() for l in text.splitlines() if l.strip()]

        for i, line in enumerate(lines):
            matches = pattern.finditer(line)
            for m in matches:
                p_type = 'Oral (口頭)' if m.group(1) == 'O' else 'Poster (壁報)'
                raw_cat = m.group(2)
                cat_code = clean_category(raw_cat)
                cat_name = CATEGORY_MAP.get(cat_code, f"{cat_code} 專題")
                pid = f"{m.group(1)}-{raw_cat}-{m.group(3)}"

                # 提取標題與前後內文
                title = ''
                if i + 1 < len(lines):
                    title = lines[i + 1]
                    if len(title) < 8 and i + 2 < len(lines):
                        title += " " + lines[i + 2]
                
                # 組合前 5 行為摘要預覽
                snippet_lines = lines[max(0, i):min(len(lines), i + 6)]
                snippet = " ".join(snippet_lines)

                extracted.append({
                    'id': pid,
                    'type': p_type,
                    'category_code': cat_code,
                    'category_name': cat_name,
                    'page': page_idx + 1,
                    'title': title.strip()[:150],
                    'snippet': snippet.strip()[:300]
                })

    # 去除重複 ID，保留資訊最完整的一筆
    unique_map = {}
    for item in extracted:
        pid = item['id']
        if pid not in unique_map:
            unique_map[pid] = item
        else:
            # 優先保留在摘要正文頁面（通常大於第 40 頁）且標題較長者
            if len(item['title']) > len(unique_map[pid]['title']) or (item['page'] > 40 and unique_map[pid]['page'] <= 40):
                unique_map[pid] = item

    papers = sorted(list(unique_map.values()), key=lambda x: (x['category_code'], x['id']))
    print(f"✅ 成功結構化萃取 {len(papers)} 篇獨立學術論文！")
    return papers

def search_abstracts(papers, query):
    q = query.lower()
    results = []
    for p in papers:
        score = 0
        search_target = f"{p['id']} {p['category_name']} {p['title']} {p['snippet']}".lower()
        if q in p['id'].lower():
            score += 10
        if q in p['title'].lower():
            score += 5
        if q in p['category_name'].lower() or q in p['category_code'].lower():
            score += 3
        if q in p['snippet'].lower():
            score += 1

        if score > 0:
            results.append((score, p))

    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results]

def export_benchmark_json(papers):
    data = {
        'is_test_benchmark': True,
        'year': 2026,
        'dataset_source': '中華民國醫事放射學會第59次年會暨國際醫學影像學術研討會論文集 (測試樣本)',
        'note': '本資料庫為 2026 測試基準，僅供大腦檢索演算法與壓力測試，嚴格與 2027 AACRT 知識大腦隔離。',
        'total_papers': len(papers),
        'categories_summary': {},
        'papers': papers
    }
    
    # 計算各分類篇數
    for p in papers:
        c = p['category_name']
        data['categories_summary'][c] = data['categories_summary'].get(c, 0) + 1

    BENCHMARK_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(BENCHMARK_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"💾 已儲存測試基準庫: {BENCHMARK_JSON.name} (共 {len(papers)} 篇)")
    return data

def main():
    papers = parse_proceedings()
    if not papers:
        return

    benchmark_data = export_benchmark_json(papers)

    print("\n==================================================")
    print("📊 2026 測試樣本論文集 - 專題分類統計表")
    print("==================================================")
    for cat, count in sorted(benchmark_data['categories_summary'].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {cat}: {count} 篇")

    # 模擬 4 大核心關鍵字檢索測試
    test_keywords = ['AI', 'CT', 'MRI', 'PSMA']
    print("\n==================================================")
    print("🔍 論文檢索測試 (Simulation Search Queries)")
    print("==================================================")
    for kw in test_keywords:
        hits = search_abstracts(papers, kw)
        print(f"\n👉 檢索關鍵字 [{kw}]: 命中 {len(hits)} 篇")
        for h in hits[:3]:
            print(f"   [{h['id']}] {h['type']} (P.{h['page']})")
            print(f"     領域: {h['category_name']}")
            print(f"     標題: {h['title']}")

if __name__ == '__main__':
    main()
