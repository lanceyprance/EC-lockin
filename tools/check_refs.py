"""Check the 📐 box numbering and every 'Rule N' / 'Equation N' reference.

Usage: python3 tools/check_refs.py
- every 📐 number is unique, and the numbers run 1..max with no gaps;
- a bare 'Rule N' / 'Equation N' in notes/NN or questions/NN must be a box in topic NN;
- 'Topic M Rule N' must be a box in topic M;
- 'Rules a to b' ranges are checked at both ends.
The site's parser treats 'Rule' and 'Equation' the same, so the kind is not checked.
"""
import re, glob, os, sys

boxes = {}  # n -> topic
bad = 0
for f in sorted(glob.glob('notes/*.md')):
    t = int(os.path.basename(f)[:2])
    for m in re.finditer(r'^###\s+📐\s+(?:Equation|Rule)\s+(\d+)', open(f).read(), re.M):
        n = int(m.group(1))
        if n in boxes:
            print(f'DUP box {n} in topic {t} and {boxes[n]}'); bad += 1
        boxes[n] = t
mx = max(boxes)
missing = [n for n in range(1, mx + 1) if n not in boxes]
if missing: print('gaps in numbering:', missing); bad += 1

ref = re.compile(r'(?:Topic\s+(\d+)[,\s]*)?(?:Equations?|Rules?)\s+(\d+)(?:\s*(?:to|and|,)\s*(\d+))?')
for f in sorted(glob.glob('notes/*.md') + glob.glob('questions/*.md')):
    here = int(os.path.basename(f)[:2])
    for ln, line in enumerate(open(f), 1):
        if line.startswith('### 📐'): continue
        for m in ref.finditer(line):
            topic = int(m.group(1)) if m.group(1) else here
            for g in (m.group(2), m.group(3)):
                if not g: continue
                n = int(g)
                if boxes.get(n) != topic:
                    print(f'{f}:{ln}: "{m.group(0)}" -> box {n} is in topic {boxes.get(n)}, not {topic}'); bad += 1
print('boxes:', len(boxes), 'max', mx, '| problems:', bad)
sys.exit(1 if bad else 0)
