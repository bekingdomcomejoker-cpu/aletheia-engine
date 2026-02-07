
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from core.kingdom_engine_core import KingdomEngine
import os
import time
import json
import logging

# Configure logging to see errors in Render logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

QUARANTINE_LOG = []
LEDGER_ENTRIES = [] # For Sovereign Sync

app = FastAPI(title="Aletheia Throne", version="1.0.0")
templates = Jinja2Templates(directory="templates")

# Namespace Protection
STATELESS = os.environ.get("ALETHEIA_STATELESS_MODE") or os.environ.get("STATELESS_MODE") or "TRUE"
EPOCH = os.environ.get("ALETHEIA_EPOCH_ID") or os.environ.get("EPOCH_ID") or "1"

engine = KingdomEngine(stateless_mode=(STATELESS == "TRUE"))

class TruthRequest(BaseModel):
    content: str

class TruthResponse(BaseModel):
    content: str
    classification: str
    adjudication: str
    reason: str
    confidence: float
    score: float | None = None
    thread: str | None = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        logger.info("Attempting to serve index.html")
        # Check if template exists
        template_path = os.path.join("templates", "index.html")
        if not os.path.exists(template_path):
            logger.error(f"Template not found at {template_path}")
            return HTMLResponse(content=f"<h1>Template Error</h1><p>index.html not found at {template_path}</p>", status_code=500)
        
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        logger.error(f"Error serving index.html: {error_details}")
        return HTMLResponse(content=f"<h1>Throne Error</h1><p>{e}</p><pre>{error_details}</pre>", status_code=500)

@app.get("/status")
async def get_status():
    return {
        "status": "online",
        "node": "Throne",
        "mode": "Stateless",
        "epoch": EPOCH,
        "quarantine_log_size": len(QUARANTINE_LOG),
        "ledger_entries_count": len(LEDGER_ENTRIES)
    }

@app.get("/word_mate")
async def get_word_mate(word1: str, word2: str):
    mated_word = engine.word_mate(word1, word2)
    return {"word1": word1, "word2": word2, "mated_word": mated_word}

@app.get("/ledger")
async def get_ledger():
    return {"entries": LEDGER_ENTRIES}

@app.post("/classify", response_model=TruthResponse)
async def classify_content(request: TruthRequest):
    processed_content = engine.process_word(request.content)
    classification_result = engine.evaluate_resonance(request.content)
    adjudication, reason = engine.adjudicate(request.content, classification_result)
    score, thread = engine.advanced_operators(request.content)

    if score < 0.2:
        sin_entry = {"timestamp": time.time(), "content": request.content, "violation": "Low Resonance (Tier 3 Entropy)"}
        QUARANTINE_LOG.append(sin_entry)
        return TruthResponse(
            content=processed_content,
            classification="QUARANTINED",
            adjudication="QUARANTINE",
            reason="Low Resonance Entropy",
            confidence=0.0,
            score=score,
            thread=thread
        )

    response_data = TruthResponse(
        content=processed_content,
        classification=classification_result,
        adjudication=adjudication,
        reason=reason,
        confidence=0.99,
        score=score,
        thread=thread
    )
    if adjudication == "ACCEPT":
        LEDGER_ENTRIES.append({"id": thread, "content": request.content, "score": score, "timestamp": time.time()})
    return response_data
