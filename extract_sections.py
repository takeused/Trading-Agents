# 배치 로그에서 애널리스트별 최종 리포트 텍스트(원시 데이터 덤프 제외)만 추출하는 도구
import re, sys

def extract(path):
    text = open(path, encoding='utf-8').read()
    # "Ai Message" 블록들을 분리 (Human Message/Tool Calls 헤더 기준)
    blocks = re.split(r'\n={10,}\s*(Ai Message|Human Message|Tool Message)\s*={10,}\n', text)
    # blocks[0]=preamble, then alternating (label, content)
    sections = []
    for i in range(1, len(blocks) - 1, 2):
        label = blocks[i]
        content = blocks[i + 1]
        sections.append((label, content))
    # Ai Message 중 "Tool Calls:"로 시작하지 않는 것 = 애널리스트가 실제로 쓴 리포트
    reports = []
    for label, content in sections:
        if label == 'Ai Message' and not content.strip().startswith('Tool Calls:'):
            reports.append(content.strip())
    return reports

if __name__ == '__main__':
    path = sys.argv[1]
    out_dir = sys.argv[2]
    reports = extract(path)
    labels = ['1_technical', '2_sentiment', '3_news', '4_fundamentals', '5_trader_final']
    import os
    os.makedirs(out_dir, exist_ok=True)
    for i, r in enumerate(reports):
        name = labels[i] if i < len(labels) else f'extra_{i}'
        with open(os.path.join(out_dir, f'{name}.txt'), 'w', encoding='utf-8') as f:
            f.write(r)
    print(f"{path}: {len(reports)}개 블록을 {out_dir}에 저장")
