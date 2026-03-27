from pydantic import BaseModel

class NoteCreate(BaseModel):
    content: str

class Note(BaseModel):
    id: int
    content: str
    summary: str

    class Config:
        orm_mode = True
