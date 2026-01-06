import os
import glob
import re

directory = r'c:\Users\hrithikesh\anokha-techfair-2026-qr'
# Expanded patterns to include ST and NST files
patterns = ['ATFE26-HT*.html', 'ATFE26-ST*.html', 'ATFE26-NST*.html']
files = []
for p in patterns:
    files.extend(glob.glob(os.path.join(directory, p)))

# specific pattern for the linkedin/team-member icon
pattern = re.compile(r'(<svg xmlns="http://www\.w3\.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill=")([^"]+)(">.*?</svg>)', re.DOTALL)

replacement_fill = "blue"

files_updated = 0

for file_path in files:
    filename = os.path.basename(file_path)
    if filename == 'ATFE26-HT01.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we have matches
    if pattern.search(content):
        new_content = pattern.sub(r'\1' + replacement_fill + r'\3', content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
            files_updated += 1
        else:
             # This might happen if it was already updated in the previous run
             pass 
    else:
        print(f"No matching icons found in {filename}")

print(f"Total files updated: {files_updated}")
