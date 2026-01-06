import os
import re

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update the HTML structure
    html_pattern = r'(\s*<div class="logo-container">\s*)<div class="logo-left"><img src="assets/BLACK LOGO\.webp" alt="Logo"></div>\s*<div class="logo-right"><img src="assets/TFE\.png" alt="Logo"></div>(\s*</div>)'
    html_replacement = r'\1<div class="logo-group">\n          <img src="assets/anokha.PNG" alt="AIC ACE">\n          <img src="assets/AIC_ACE.png" alt="Anokha">\n          <img src="assets/IIC.png" alt="TechFair">\n        </div>\n        <div class="logo-bottom">\n          <img src="assets/TFE.png" alt="Logo">\n        </div>\2'

    content = re.sub(html_pattern, html_replacement, content, flags=re.MULTILINE | re.DOTALL)

    # Update the CSS
    css_pattern = r'(\s*\.logo-container \{\s*display: flex;\s*align-items: center;\s*gap: 20px;\s*margin-bottom: 30px;\s*width: fit-content;\s*\}\s*\.logo-left,\s*\.logo-right \{\s*background: white;\s*border-radius: 10px;\s*padding: 10px;\s*display: flex;\s*align-items: center;\s*justify-content: center;\s*box-shadow: 0 3px 10px rgba\(0, 0, 0, 0\.2\);\s*\}\s*\.logo-left img,\s*\.logo-right img \{\s*height: 60px;\s*width: auto;\s*max-width: 100%;\s*object-fit: contain;\s*display: block;\s*\})'

    css_replacement = r'''    .logo-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 15px;
      margin-bottom: 30px;
      width: 100%;
    }

    .logo-group {
      background: white;
      border-radius: 10px;
      padding: 8px 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
      max-width: 100%;
      width: 100%;
      flex-wrap: nowrap;
      box-sizing: border-box;
    }

    .logo-group img {
      max-height: 55px;
      width: auto;
      max-width: 30%;
      /* Ensure 3 logos fit */
      object-fit: contain;
      flex-shrink: 1;
    }

    .logo-bottom {
      background: white;
      border-radius: 10px;
      padding: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
      width: fit-content;
    }

    .logo-bottom img {
      height: 60px;
      width: auto;
      object-fit: contain;
      display: block;
    }'''

    content = re.sub(css_pattern, css_replacement, content, flags=re.MULTILINE | re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath}")

def main():
    # Get all HTML files in current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f.startswith('ATFE26-')]

    for html_file in html_files:
        try:
            update_html_file(html_file)
        except Exception as e:
            print(f"Error updating {html_file}: {e}")

if __name__ == "__main__":
    main()
