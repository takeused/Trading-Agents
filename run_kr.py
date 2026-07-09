# 한국 주식 1종목을 Cerebras LLM으로 분석해 최종 매매 판단을 출력하는 실행 스크립트
# 설정은 .env(TRADINGAGENTS_* / OPENAI_COMPATIBLE_API_KEY)에서 자동 로드됩니다.
import sys

# Windows cp949 콘솔에서 유니코드 특수문자(—, → 등) 출력 시 UnicodeEncodeError 방지
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 기본값: 삼성전자, 분석 기준일. 커맨드라인 인자로 덮어쓸 수 있습니다.
#   python run_kr.py 000660.KS 2026-06-30
ticker = sys.argv[1] if len(sys.argv) > 1 else "005930.KS"
trade_date = sys.argv[2] if len(sys.argv) > 2 else "2026-06-30"

config = DEFAULT_CONFIG.copy()  # .env의 TRADINGAGENTS_* 값이 이미 반영되어 있음

print(f"[설정] provider={config['llm_provider']} / deep={config['deep_think_llm']} / "
      f"quick={config['quick_think_llm']} / lang={config['output_language']}")
print(f"[분석] {ticker} @ {trade_date} 시작. 에이전트가 순차 실행되어 수 분 소요됩니다.\n")

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate(ticker, trade_date)

print("\n" + "=" * 60)
print("최종 매매 판단")
print("=" * 60)
print(decision)
