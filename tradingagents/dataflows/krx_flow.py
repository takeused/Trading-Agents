import logging
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

logger = logging.getLogger(__name__)

def clean_ticker(ticker: str) -> str:
    """영문 티커(005930.KS, 005930)에서 6자리 숫자만 추출"""
    match = re.search(r'\d{6}', ticker)
    return match.group(0) if match else ticker

def fetch_krx_investor_flow(ticker: str, end_date_str: str, limit: int = 5) -> str:
    """네이버 금융 외국인/기관 매매동향 페이지에서 분석 기준일(end_date_str) 이전의 수급 데이터를 추출합니다."""
    code = clean_ticker(ticker)
    
    # 국내 종목이 아니면 빈 문자열 반환
    if not code.isdigit():
        return ""
        
    url = f"https://finance.naver.com/item/frgn.naver?code={code}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"KRX 수급 수집 실패 (HTTP {response.status_code})"
            
        response.encoding = "euc-kr"
        soup = BeautifulSoup(response.text, "html.parser")
        
        # '외국인 기관 순매매 거래량' 표 찾기
        table = soup.find("table", summary=lambda s: s and "외국인 기관" in s)
        if not table:
            return "KRX 수급 분석 테이블을 찾을 수 없습니다."
            
        rows = table.find_all("tr")
        flow_data = []
        
        target_date_limit = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        for row in rows:
            cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
            
            # 유효한 데이터 행 검사 (날짜 포맷: YYYY.MM.DD)
            if len(cols) >= 7:
                date_text = cols[0]
                if re.match(r'^\d{4}\.\d{2}\.\d{2}$', date_text):
                    # 날짜 객체로 변환
                    row_date = datetime.strptime(date_text, "%Y.%m.%d")
                    # 분석 기준일(end_date_str)과 같거나 과거인 데이터만 포함
                    if row_date <= target_date_limit:
                        flow_data.append({
                            "date": row_date.strftime("%Y-%m-%d"),
                            "close": cols[1],
                            "volume": cols[4],
                            "institution": cols[5],
                            "foreigner": cols[6]
                        })
                        if len(flow_data) >= limit:
                            break
                            
        if not flow_data:
            return f"기준일 {end_date_str} 이전의 수급 데이터를 찾을 수 없습니다."
            
        # 마크업 표 작성
        flow_lines = [
            f"### [KRX 투자자별 수급 동향] (기준일 {end_date_str} 이전 {len(flow_data)}일 누적)",
            "| 날짜 | 종가 (원) | 거래량 (주) | 기관 순매매 (주) | 외국인 순매매 (주) |",
            "| :--- | :---: | :---: | :---: | :---: |"
        ]
        
        for data in flow_data:
            flow_lines.append(
                f"| {data['date']} | {data['close']} | {data['volume']} | {data['institution']} | {data['foreigner']} |"
            )
            
        # 당일(가장 최신 수집된 당일) 요약
        today_data = flow_data[0]
        flow_lines.append(f"\n💡 **분석 당일 수급 특이사항**: 기관 {today_data['institution']}주, 외국인 {today_data['foreigner']}주 순매매 기록.")
        
        return "\n".join(flow_lines)
        
    except Exception as e:
        logger.error("KRX flow fetch error: %s", e)
        return f"KRX 수급 데이터를 추출하는 중 오류 발생: {str(e)}"

# 직접 실행 테스트용
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(fetch_krx_investor_flow("005930.KS", "2026-06-30"))
