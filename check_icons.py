import os
import glob
import re

directory = r'c:\Users\hrithikesh\anokha-techfair-2026-qr'
files = glob.glob(os.path.join(directory, 'ATFE26-HT*.html'))
pattern = re.compile(r'<svg[^>]*width="20"[^>]*height="20"[^>]*>')

stats = {}

for file_path in files:
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    for match in matches:
        if match not in stats:
            stats[match] = 0
        stats[match] += 1

print("Found SVG variants:")
for svg, count in stats.items():
    print(f"Count: {count} | SVG: {svg}")
