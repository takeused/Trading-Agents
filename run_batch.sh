#!/usr/bin/env bash
# 포털 등재 6종목을 지정 기준일로 순차 분석해 원본 로그를 _runs/<날짜>/ 에 저장하는 배치 러너
DATE="${1:-2026-07-20}"
OUT="_runs/$DATE"
mkdir -p "$OUT"

# "티커:파일명" 매핑 (파일명은 reports/ 하위 리포트 파일명 규칙과 동일)
PAIRS="005930.KS:samsung 000660.KS:sk_hynix 214150.KQ:classys 105560.KS:kb_financial 200670.KQ:humedix 483650.KS:dalba"

for p in $PAIRS; do
  TICKER="${p%%:*}"
  NAME="${p##*:}"
  echo "=== [$(date +%H:%M:%S)] $NAME ($TICKER) 시작 ==="
  PYTHONIOENCODING=utf-8 .venv/Scripts/python.exe run_kr.py "$TICKER" "$DATE" > "$OUT/$NAME.log" 2>&1
  echo "=== [$(date +%H:%M:%S)] $NAME 완료 (exit=$?) / $(wc -l < "$OUT/$NAME.log") lines ==="
done

echo "=== 전체 배치 완료 ==="
