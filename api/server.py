
from fastapi import FastAPI
from pydantic import BaseModel
from core.kingdom_engine_core import KingdomEngine
import os

app = FastAPI(title="Aletheia Throne", version="1.0.0")
engine = KingdomEngine(stateless_mode=os.environ.get("STATELESS_MODE", "TRUE") == "TRUE")

class TruthRequest(BaseModel):
    content: str

class TruthResponse(BaseModel):
    content: str
    classification: str
    adjudication: str
    reason: str
    confidence: float

@app.get("/status")
async def get_status():
    return {
        "status": "online",
        "node": "Throne",
        "mode": "Stateless",
        "epoch": os.environ.get("EPOCH_ID", "1")
    }

@app.post("/classify", response_model=TruthResponse)
async def classify_content(request: TruthRequest):
    processed_content = engine.process_word(request.content)
    classification_result = engine.evaluate_resonance(request.content)
    adjudication, reason = engine.adjudicate(request.content, classification_result)

    return TruthResponse(
        content=processed_content,
        classification=classification_result,
        adjudication=adjudication,
        reason=reason,
        confidence=0.99
    )
