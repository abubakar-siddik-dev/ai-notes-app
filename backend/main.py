from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, Base
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 👉 FREE AI API (HuggingFace)
def generate_summary(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer YOUR_HF_API_KEY"}  # replace

    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    try:
        return response.json()[0]['summary_text']
    except:
        return "Summary failed"

# ➕ Add note
@app.post("/notes/")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    summary = generate_summary(note.content)

    new_note = models.Note(
        content=note.content,
        summary=summary
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# 📋 Get all notes
@app.get("/notes/")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()

# ❌ Delete
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).get(note_id)
    db.delete(note)
    db.commit()
    return {"msg": "Deleted"}
