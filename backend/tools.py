from db import SessionLocal
from models import Interaction

# Tool 1: Log Interaction
def log_interaction(data):
    db = SessionLocal()
    interaction = Interaction(
        doctor_name=data["doctor_name"],
        date=data["date"],
        notes=data["notes"],
        summary=data["summary"]
    )
    db.add(interaction)
    db.commit()
    return "Interaction Saved"


# Tool 2: Edit Interaction
def edit_interaction(id, data):
    db = SessionLocal()
    interaction = db.query(Interaction).filter(Interaction.id == id).first()
    if interaction:
        interaction.notes = data["notes"]
        interaction.summary = data["summary"]
        db.commit()
        return "Updated"
    return "Not Found"


# Tool 3: Search Interaction
def search_interaction(name):
    db = SessionLocal()
    results = db.query(Interaction).filter(Interaction.doctor_name == name).all()
    return [r.notes for r in results]


# Tool 4: Suggest Action
def suggest_action(summary):
    return "Follow-up meeting recommended"


# Tool 5: Generate Report
def generate_report():
    return "Basic report generated"