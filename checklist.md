# 날짜별 리포트 이력 관리 — 체크리스트

## 목표
리포트를 날짜별로 보관하고 index.html 드롭다운으로 기준일별 확인.

## 구조 (결정)
```
reports/
  data.js                  # window.TA_DATA = {overviews, reports[]} (script src, file:// 오프라인 동작)
  2026-06-30/{samsung,sk_hynix,classys,kb_financial}.{html,md}
  2026-07-10/{dalba,humedix}.{html,md}
index.html                 # 날짜 드롭다운 → 해당 날짜 카드/요약 렌더
```

## 작업
- [x] reports/2026-06-30, reports/2026-07-10 디렉토리 생성
- [x] 기존 6개 리포트 html/md 이동 + 리네이밍 ({종목}_analysis_report → {종목})
- [x] 이동한 리포트 내부 링크 수정: index.html → ../../index.html (promo-banner, top-nav 각 2곳)
- [x] reports/data.js 작성 (6개 리포트 메타 + 날짜별 overview)
- [x] index.html 재작성: 날짜 드롭다운 + data.js 기반 동적 카드 렌더 (최신 날짜 기본)
- [x] 검증: 모의 DOM 렌더 통과 (07-10 카드 2·필터 3, 06-30 카드 4·필터 5, 런타임 오류 없음), href 대상·복귀 링크 정상

## 향후 신규 리포트 추가 절차 (문서화)
1. run_kr.py 실행 → 리포트 html/md 작성
2. reports/{기준일}/ 에 {종목}.html, {종목}.md 저장
3. data.js의 reports[]에 항목 추가, overviews에 날짜 요약 추가
