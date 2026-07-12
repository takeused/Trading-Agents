// 날짜별 리포트 메타데이터 — 포털 index.html이 <script src>로 로드하여 드롭다운/카드를 렌더한다.
// 신규 리포트 추가 시: reports/{기준일}/{종목}.html·md 저장 후, 아래 reports[]에 항목 추가 + overviews에 날짜 요약 추가.
window.TA_DATA = {

  // 날짜별 포트폴리오 요약 (해당 기준일에 분석한 종목 기준)
  overviews: {
    "2026-07-10":
      '• <strong>[신규]</strong> 소비재·헬스케어 2종목을 신규 분석했습니다. <br>' +
      '• <strong>휴메딕스</strong>는 Forward PE 6.6배·배당 4.2%·시총 42% 현금이라는 방패에 기관 5일 연속 순매수+외국인 합류·MACD 골든크로스 태동이 겹쳐 ' +
      '<strong>Overweight</strong>를 획득했습니다. 50·200일선 저항을 감안해 현재가(2.69만 원) 정찰 매수 후 <strong>50일선 돌파 확인 시 2~3%까지 점진적 증량</strong>이 유효합니다. <br>' +
      '• <strong>달바글로벌</strong>은 ROE 50.8%·PE 13.8배의 경이적 펀더멘털에도 10일·50일선 동반 하향 돌파와 기관 순매도 우세로 단기 추세가 붕괴돼 ' +
      '<strong style="color:var(--colors-critical);">Underweight (비중 축소)</strong>로 분류됐습니다. 50일선(21.6만 원) 회복 + MACD 양전 전까지 <strong>비중 5% 이하 축소</strong>로 리스크 관리를 우선합니다.',
    "2026-06-30":
      '• <strong>삼성전자</strong>, <strong>SK하이닉스</strong>, <strong>클래시스</strong>, <strong>KB금융</strong> 네 종목 모두 실적 성장성과 밸류에이션 저평가 매력으로 ' +
      '<strong>Overweight (비중 확대)</strong> 결정을 획득했습니다. <br>' +
      '• 반도체 대형주는 단기 데드크로스와 외인 차익 매도세가 하방 압력으로 작용 중이므로 <strong>50일 이동평균선(삼성 29.1만·하이닉스 213.6만 원 선) 부근 분할 매수</strong>를 제안합니다. <br>' +
      '• 미용 의료기기 1위 <strong>클래시스</strong>는 고마진(영업이익률 42%)·바닥권 골든크로스로 현재가(4.6만 원 대)에서 <strong>5~7% 공격적 분할 진입</strong>이 유효합니다. <br>' +
      '• 금융 대장주 <strong>KB금융</strong>은 자사주 소각·밸류업 최대 수혜로 외인/기관 쌍끌이 순매수가 유입, 현재가(15.9만 원 선)에서 <strong>8~10% 편입</strong>이 매력적입니다.'
  },

  // 리포트 카드 (최신 날짜가 위로 오도록 배열; 같은 날짜 내 표시 순서 = 배열 순서)
  reports: [
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
