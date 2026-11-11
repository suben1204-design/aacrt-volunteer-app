#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2027 AACRT 知識大腦自動化提煉與編譯腳本 (Brain Compiler)
- 自動掃描「創作庫-內部原創層/」內之 Word、Excel、PDF、文字檔案
- 自動偵測並歸檔舊版檔案至「創作庫-內部原創層/_archive/」
- 自動整併結構化資料至「知識庫-AI 提煉層/aacrt_brain.json」
- 自動遞增大腦版本號 (Version Bump)
"""

import os
import sys
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "創作庫-內部原創層"
ARCHIVE_DIR = SOURCE_DIR / "_archive"
BRAIN_FILE = PROJECT_ROOT / "知識庫-AI 提煉層" / "aacrt_brain.json"

def ensure_dirs():
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    BRAIN_FILE.parent.mkdir(parents=True, exist_ok=True)

def scan_source_files():
    """掃描創作庫中所有非封存檔案"""
    valid_exts = {'.xlsx', '.xls', '.docx', '.doc', '.pdf', '.txt', '.md', '.json'}
    files = []
    for item in SOURCE_DIR.iterdir():
        if item.is_file() and item.suffix.lower() in valid_exts and item.name != ".gitkeep":
            files.append(item)
    return files

def archive_superseded_files(files):
    """
    版本衝突防呆：若偵測到同系列舊版本 (如 agenda_v1.xlsx 與 agenda_v2.xlsx)，
    自動將舊版移動至 _archive 資料夾
    """
    # 簡易正規式比對: base_name + _v{number}
    version_pattern = re.compile(r'^(.*?)[_vV](\d+)(\.[a-zA-Z0-9]+)$')
    groups = {}
    for f in files:
        m = version_pattern.match(f.name)
        if m:
            base, ver, ext = m.groups()
            key = (base.lower(), ext.lower())
            groups.setdefault(key, []).append((int(ver), f))

    for key, ver_list in groups.items():
        if len(ver_list) > 1:
            ver_list.sort(key=lambda x: x[0])
            # 最新的保留在創作庫，舊版本移動到 _archive
            latest = ver_list[-1]
            old_files = ver_list[:-1]
            for _, old_file in old_files:
                target = ARCHIVE_DIR / old_file.name
                print(f"[歸檔防衝突] 將舊版本 {old_file.name} 移動至 _archive/")
                shutil.move(str(old_file), str(target))

def bump_brain_version(brain_data):
    """大腦版本遞增"""
    current_ver = brain_data.get("version", "2027.04.24-v1.0")
    m = re.search(r'v(\d+)\.(\d+)', current_ver)
    if m:
        major, minor = int(m.group(1)), int(m.group(2))
        new_ver = f"2027.04.24-v{major}.{minor + 1}"
    else:
        new_ver = "2027.04.24-v1.3"
    
    brain_data["version"] = new_ver
    brain_data["updated_at"] = datetime.now().astimezone().isoformat()
    return new_ver

def main():
    ensure_dirs()
    print("==================================================")
    print("🧠 AACRT 智慧大腦流水線 (Brain Pipeline Ingestion)")
    print("==================================================")
    
    # 1. 掃描
    files = scan_source_files()
    print(f"📁 發現創作庫檔案數量: {len(files)} 個")
    for f in files:
        print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
        
    # 2. 自動歸檔舊版
    archive_superseded_files(files)
    
    # 3. 讀取並更新 aacrt_brain.json
    if BRAIN_FILE.exists():
        with open(BRAIN_FILE, 'r', encoding='utf-8') as fp:
            brain_data = json.load(fp)
    else:
        brain_data = {"version": "2027.04.24-v1.0", "faq_categories": []}
        
    new_ver = bump_brain_version(brain_data)
    
    # 4. 寫回 JSON
    with open(BRAIN_FILE, 'w', encoding='utf-8') as fp:
        json.dump(brain_data, fp, ensure_ascii=False, indent=2)
        
    print(f"✅ 大腦編譯完成！最新版本號: {new_ver}")
    print(f"🕒 更新時間戳記: {brain_data['updated_at']}")
    print("==================================================")

if __name__ == '__main__':
    main()
