
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
    # This is a placeholder for actual classification logic
    # In a real scenario, the engine would process the content and return a classification
    processed_content = engine.process_word(request.content)
    classification_result = engine.evaluate_resonance(request.content)

    return TruthResponse(
        content=processed_content,
        classification=classification_result,
        confidence=0.99 # Placeholder confidence
    )
