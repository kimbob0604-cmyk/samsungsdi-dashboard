"""src/ + data/ → docs/index.html 빌드"""
import json
from pathlib import Path
R = Path(__file__).parent
css = (R/'src/css.part').read_text(encoding='utf-8')
body = (R/'src/body.part').read_text(encoding='utf-8')
px = (R/'data/px.json').read_text(encoding='utf-8')
peers = json.dumps(json.loads((R/'data/peers.json').read_text(encoding='utf-8')), ensure_ascii=False)
head = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>삼성SDI 대시보드</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
'''
(R/'docs/index.html').write_text(head + css + '\n' + body.replace('/*__PX__*/null', px).replace('/*__PEERS__*/null', peers), encoding='utf-8')
print('built docs/index.html')
