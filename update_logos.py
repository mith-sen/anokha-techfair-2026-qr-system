import os
import re

def update_logo_alts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the correct alt texts
    alt_updates = {
        'assets/anokha.PNG': 'Anokha',
        'assets/AIC_ACE.png': 'AIC ACE',
        'assets/IIC.png': 'IIC',
        'assets/TFE.png': 'TFE'
    }

    # Update each logo's alt text
    for src, alt in alt_updates.items():
        # Find the img tag with the src and update the alt
        pattern = rf'(<img src="{re.escape(src)}" alt=")[^"]*(">)'
        replacement = rf'\1{alt}\2'
        content = re.sub(pattern, replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated logos in {file_path}")

def main():
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f.startswith('ATFE26-')]

    for file in html_files:
        update_logo_alts(file)

if __name__ == "__main__":
    main()
