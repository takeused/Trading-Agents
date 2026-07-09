import logging
import re
import xml.etree.ElementTree as ET
import requests
from pykrx import stock

logger = logging.getLogger(__name__)

def clean_ticker(ticker: str) -> str:
    """영문 티커(005930.KS, 005930)에서 6자리 숫자만 추출"""
    match = re.search(r'\d{6}', ticker)
    return match.group(0) if match else ticker

def get_korean_name(ticker: str) -> str:
    """티커 코드를 한글 종목명으로 변환 (예: 005930 -> 삼성전자)"""
    code = clean_ticker(ticker)
    try:
        # pykrx를 이용해 종목 이름 조회
        name = stock.get_market_ticker_name(code)
        if name:
            return name
    except Exception as e:
        logger.warning("Failed to map ticker via pykrx: %s", e)
    return ticker

def fetch_naver_news(ticker: str, limit: int = 15) -> str:
    """구글 뉴스 RSS 서비스를 활용하여 신뢰성 높고 안전하게 국내 한글 주식 뉴스를 가져옵니다."""
    keyword = get_korean_name(ticker)
    
    # 구글 뉴스 RSS 한글 검색 피드 URL
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"한글 뉴스 수집 실패 (HTTP {response.status_code})"
            
        # XML RSS 파싱
        root = ET.fromstring(response.content)
        news_items = []
        
        # item 노드 추출
        for item in root.findall(".//item"):
            title = item.find("title")
            pub_date = item.find("pubDate")
            source = item.find("source")
            
            title_text = title.text if title is not None else ""
            date_text = pub_date.text if pub_date is not None else ""
            source_text = source.text if source is not None else "알수없음"
            
            # 날짜 포맷 정리 (예: Thu, 09 Jul 2026 08:00:00 GMT -> 간단히 연월일 표시)
            # RSS pubDate 예시: Thu, 09 Jul 2026 08:00:00 GMT
            try:
                # 간단한 정규식이나 문자열 파싱으로 날짜 가독성 향상
                date_match = re.search(r'\d{2}\s[A-Za-z]{3}\s\d{4}', date_text)
                if date_match:
                    date_text = date_match.group(0)
            except Exception:
                pass
                
            news_items.append(f"[{date_text}] {title_text} ({source_text})")
            if len(news_items) >= limit:
                break
                
        if not news_items:
            return f"'{keyword}'에 대한 수집된 한글 뉴스가 없습니다."
            
        return "\n".join(news_items)
        
    except Exception as e:
        logger.error("Korean news fetch error: %s", e)
        return f"한글 뉴스 수집 중 오류 발생: {str(e)}"

# 간단한 모듈 직접 실행 테스트용
if __name__ == "__main__":
    import sys
    # stdout 인코딩 설정
    sys.stdout.reconfigure(encoding='utf-8')
    print(fetch_naver_news("005930.KS"))
