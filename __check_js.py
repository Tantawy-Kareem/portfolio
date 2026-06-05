import re
from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
match = re.search(r'<script>(.*?)</script>', text, re.S)
if not match:
    print('NO_SCRIPT')
    raise SystemExit(1)
js = match.group(1)
print('BRACES', js.count('{'), js.count('}'))
# print first error line by naive detection of unclosed structures
lines = js.splitlines()
for i, line in enumerate(lines, 1):
    if 'clone.style.zIndex' in line:
        print('FOUND', i, line)
        break
