#!/usr/bin/env bash
# 2026-07-20 배치의 남은 3종목(KB금융/휴메딕스/달바글로벌)을 재개 실행.
# 지난번 3종목 연속 실행 후 429 레이트리밋이 나타나 종목 사이에 텀을 둠.
DATE="${1:-2026-07-20}"
OUT="_runs/$DATE"
mkdir -p "$OUT"

PAIRS="105560.KS:kb_financial 200670.KQ:humedix 483650.KS:dalba"

for p in $PAIRS; do
  TICKER="${p%%:*}"
  NAME="${p##*:}"
  echo "=== [$(date +%H:%M:%S)] $NAME ($TICKER) 시작 ==="
  PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe run_kr.py "$TICKER" "$DATE" > "$OUT/$NAME.log" 2>&1
  echo "=== [$(date +%H:%M:%S)] $NAME 완료 (exit=$?) / $(wc -l < "$OUT/$NAME.log") lines ==="
  echo "레이트리밋 완화를 위해 30초 대기..."
  sleep 30
done

echo "=== 재개 배치 완료 ==="
