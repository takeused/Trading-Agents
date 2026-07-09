# Cerebras 엔드포인트에서 실제 사용 가능한 모델 ID 목록을 조회하는 확인용 스크립트
import os
import urllib.request
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))

key = os.environ.get("OPENAI_COMPATIBLE_API_KEY", "")
base = os.environ.get("TRADINGAGENTS_LLM_BACKEND_URL", "https://api.cerebras.ai/v1")

if not key or key.startswith("여기에"):
    raise SystemExit("OPENAI_COMPATIBLE_API_KEY가 .env에 설정되지 않았습니다.")

req = urllib.request.Request(
    base.rstrip("/") + "/models",
    headers={"Authorization": f"Bearer {key}"},
)
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.load(resp)

print("사용 가능한 Cerebras 모델 ID.")
for m in data.get("data", []):
    print(" -", m.get("id"))
