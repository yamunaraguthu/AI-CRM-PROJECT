from langgraph_agent import graph
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
from tools import log_interaction, edit_interaction
from agent import summarize_text

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "CRM Backend Running"}


@app.post("/log")
def log(data: dict):
    summary = summarize_text(data["notes"])
    data["summary"] = summary
    result = log_interaction(data)
    return {
        "msg": result,
        "summary": summary
    }


@app.put("/edit/{id}")
def edit(id: int, data: dict):
    result = edit_interaction(id, data)
    return {"msg": result}


@app.post("/chat")
def chat(data: dict):
    result = graph.invoke(data)
    return result

@app.get("/history")
def get_history():
    from db import SessionLocal
    from models import Interaction

    db = SessionLocal()
    data = db.query(Interaction).all()

    result = []
    for item in data:
        result.append({
            "id": item.id,
            "doctor_name": item.doctor_name,
            "notes": item.notes,
            "summary": item.summary
        })

    return result