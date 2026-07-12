# Context Notes — 날짜별 리포트 이력 관리

## 배경
리포트가 `{종목}_analysis_report.html` 단일 파일이라 재생성 시 이전 날짜가 덮어써져 이력이 사라졌다.
원천 데이터(`~/.tradingagents/logs/{ticker}/TradingAgentsStrategy_logs/full_states_log_{date}.json`)는
이미 날짜별로 보관되므로, 소실되는 건 프레젠테이션 계층(html/md)뿐이었다.

## 설계 결정
- **저장 구조**: `reports/{기준일}/{종목}.html·md` (날짜 폴더 분리). 사용자 선택.
- **포털**: `index.html`에 기준일 드롭다운. 선택 날짜의 카드/요약만 렌더.
- **데이터 로딩**: `reports/data.js`를 `<script src>`로 로드. → **이유**: 사용자가 index.html을
  브라우저 더블클릭(`file://`)으로 열기 때문에 `fetch()`는 CORS로 차단됨. script 태그는 file://에서도 동작.
- **UNDERWEIGHT 표기**: `.decision-badge.underweight`(빨강) + 카드 emoji 🔴. 달바글로벌이 최초 사례.

## data.js 스키마
```
window.TA_DATA = {
  overviews: { "YYYY-MM-DD": "<html 요약 문자열>" },
  reports: [ { date, key, name, ticker, exchange, price, decision, href, specs:[{val,lbl,hl}] } ]
}
```
- `decision`: "OVERWEIGHT" | "UNDERWEIGHT" (index가 emoji/뱃지색 자동 결정)
- `hl`: spec 값 녹색 강조 여부
- `href`: index.html 기준 상대경로 (`reports/{date}/{key}.html`)
- 카드 표시 순서 = 배열 순서. 드롭다운은 날짜 최신순 자동 정렬.

## 신규 리포트 추가 절차
1. `run_kr.py {ticker} {date}` 실행 → 상태 JSON 생성
2. JSON 읽어 `reports/{date}/{종목}.html·md` 작성 (기존 리포트 템플릿 복제, 내부 링크는 `../../index.html`)
3. `reports/data.js`의 `reports[]`에 항목 추가 + `overviews`에 해당 날짜 요약 추가
   - 새 날짜면 드롭다운·overview 자동 반영됨(코드 수정 불필요)

## 검증 방법
- data.js 문법: `node -e "global.window={};require('./reports/data.js');..."`
- 렌더 로직: 모의 DOM으로 IIFE eval 실행 (checklist 참고). 브라우저 file:// 프리뷰는 확장 이슈로 타임아웃된 이력 있음.

## 주의
- 리포트 html의 promo-banner(`href`)와 top-nav(`onclick location.href`) 2곳이 포털로 돌아가는 링크.
  reports/{date}/ 안에 있으므로 반드시 `../../index.html`.
