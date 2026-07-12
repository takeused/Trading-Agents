// 날짜별 리포트 메타데이터 — 포털 index.html이 <script src>로 로드하여 드롭다운/카드를 렌더한다.
// 신규 리포트 추가 시: reports/{기준일}/{종목}.html·md 저장 후, 아래 reports[]에 항목 추가 + overviews에 날짜 요약 추가.
window.TA_DATA = {

  // 날짜별 포트폴리오 요약 (해당 기준일에 분석한 종목 기준)
  overviews: {
    "2026-07-10":
      '• <strong>[신규 & 업데이트]</strong> 기존 분석 4종목을 업데이트하고 소비재·헬스케어 2종목을 추가하여 총 6개 종목의 분석을 진행했습니다. <br>' +
      '• <strong>삼성전자</strong>(Fwd PE 4.38배)와 <strong>SK하이닉스</strong>(영업이익률 71.5%, 나스닥 상장 성공)는 단기 하락 조정세에도 압도적 펀더멘털과 저평가 메리트로 <strong>Overweight</strong>를 유지하며, 분할 매수 진입이 유효합니다. <br>' +
      '• <strong>클래시스</strong>는 고마진(영업이익률 42.7%) 및 단기 골든크로스 태동으로 <strong>Overweight</strong>를 획득, 4.8만 원 선에서 분할 진입이 매력적입니다. <br>' +
      '• <strong>KB금융</strong>은 밸류업 프로그램 및 금리 지연 수혜(동결 확률 78%)에 따른 기관/외인 동반 매수로 <strong>Overweight</strong>를 기록, 17.5~18만 원 선 지지선 대기가 유효합니다. <br>' +
      '• <strong>휴메딕스</strong>는 Forward PE 6.6배·배당 4.2%·시총 42% 현금이라는 방패를 확보해 <strong>Overweight</strong>를, <strong>달바글로벌</strong>은 단기 기술 추세 붕괴로 <strong style="color:var(--colors-critical);">Underweight (비중 축소)</strong>로 분류됐습니다.',
    "2026-06-30":
      '• <strong>삼성전자</strong>, <strong>SK하이닉스</strong>, <strong>클래시스</strong>, <strong>KB금융</strong> 네 종목 모두 실적 성장성과 밸류에이션 저평가 매력으로 ' +
      '<strong>Overweight (비중 확대)</strong> 결정을 획득했습니다. <br>' +
      '• 반도체 대형주는 단기 데드크로스와 외인 차익 매도세가 하방 압력으로 작용 중이므로 <strong>50일 이동평균선(삼성 29.1만·하이닉스 213.6만 원 선) 부근 분할 매수</strong>를 제안합니다. <br>' +
      '• 미용 의료기기 1위 <strong>클래시스</strong>는 고마진(영업이익률 42%)·바닥권 골든크로스로 현재가(4.6만 원 대)에서 <strong>5~7% 공격적 분할 진입</strong>이 유효합니다. <br>' +
      '• 금융 대장주 <strong>KB금융</strong>은 자사주 소각·밸류업 최대 수혜로 외인/기관 쌍끌이 순매수가 유입, 현재가(15.9만 원 선)에서 <strong>8~10% 편입</strong>이 매력적입니다.'
  },

  // 리포트 카드 (최신 날짜가 위로 오도록 배열; 같은 날짜 내 표시 순서 = 배열 순서)
  reports: [
    { date: "2026-07-10", key: "samsung", name: "삼성전자", ticker: "005930.KS", exchange: "KOSPI",
      price: "285,000 KRW", decision: "OVERWEIGHT", href: "reports/2026-07-10/samsung.html",
      specs: [ {val:"4.38배",lbl:"Forward PE",hl:true}, {val:"18.86%",lbl:"ROE",hl:false}, {val:"42.75%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-07-10", key: "hynix", name: "SK하이닉스", ticker: "000660.KS", exchange: "KOSPI",
      price: "2,180,000 KRW", decision: "OVERWEIGHT", href: "reports/2026-07-10/sk_hynix.html",
      specs: [ {val:"4.86배",lbl:"Forward PE",hl:true}, {val:"61.17%",lbl:"ROE",hl:true}, {val:"71.54%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-07-10", key: "classys", name: "클래시스", ticker: "214150.KQ", exchange: "KOSDAQ",
      price: "48,500 KRW", decision: "OVERWEIGHT", href: "reports/2026-07-10/classys.html",
      specs: [ {val:"13.69배",lbl:"Forward PE",hl:true}, {val:"27.19%",lbl:"ROE",hl:true}, {val:"42.67%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-07-10", key: "kb", name: "KB금융", ticker: "105560.KS", exchange: "KOSPI",
      price: "184,400 KRW", decision: "OVERWEIGHT", href: "reports/2026-07-10/kb_financial.html",
      specs: [ {val:"9.46배",lbl:"Forward PE",hl:true}, {val:"9.99%",lbl:"ROE",hl:true}, {val:"36.58%",lbl:"순이익률",hl:false} ] },

    { date: "2026-07-10", key: "humedix", name: "휴메딕스", ticker: "200670.KQ", exchange: "KOSDAQ",
      price: "26,900 KRW", decision: "OVERWEIGHT", href: "reports/2026-07-10/humedix.html",
      specs: [ {val:"6.60배",lbl:"Forward PE",hl:true}, {val:"4.16%",lbl:"배당수익률",hl:true}, {val:"15.38%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-07-10", key: "dalba", name: "달바글로벌", ticker: "483650.KS", exchange: "KOSPI",
      price: "197,900 KRW", decision: "UNDERWEIGHT", href: "reports/2026-07-10/dalba.html",
      specs: [ {val:"13.82배",lbl:"Forward PE",hl:true}, {val:"50.85%",lbl:"ROE",hl:true}, {val:"26.33%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-06-30", key: "samsung", name: "삼성전자", ticker: "005930.KS", exchange: "KOSPI",
      price: "334,000 KRW", decision: "OVERWEIGHT", href: "reports/2026-06-30/samsung.html",
      specs: [ {val:"4.24배",lbl:"Forward PE",hl:true}, {val:"18.86%",lbl:"ROE",hl:false}, {val:"42.75%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-06-30", key: "hynix", name: "SK하이닉스", ticker: "000660.KS", exchange: "KOSPI",
      price: "2,650,000 KRW", decision: "OVERWEIGHT", href: "reports/2026-06-30/sk_hynix.html",
      specs: [ {val:"4.91배",lbl:"Forward PE",hl:true}, {val:"61.17%",lbl:"ROE",hl:true}, {val:"71.50%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-06-30", key: "classys", name: "클래시스", ticker: "214150.KQ", exchange: "KOSDAQ",
      price: "46,600 KRW", decision: "OVERWEIGHT", href: "reports/2026-06-30/classys.html",
      specs: [ {val:"14.14배",lbl:"Forward PE",hl:true}, {val:"27.19%",lbl:"ROE",hl:true}, {val:"42.67%",lbl:"영업이익률",hl:false} ] },

    { date: "2026-06-30", key: "kb", name: "KB금융", ticker: "105560.KS", exchange: "KOSPI",
      price: "159,000 KRW", decision: "OVERWEIGHT", href: "reports/2026-06-30/kb_financial.html",
      specs: [ {val:"7.20배",lbl:"Forward PE",hl:true}, {val:"13.94%",lbl:"ROE",hl:true}, {val:"39.30%",lbl:"CIR(비용비율)",hl:false} ] }
  ]
};
