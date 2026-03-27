from sqlalchemy import Column, Integer, String
from database import Base

class Note(Base):
    tablename = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    summary = Column(String)
