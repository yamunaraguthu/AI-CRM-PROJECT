from sqlalchemy import Column, Integer, String
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    date = Column(String)
    notes = Column(String)
    summary = Column(String)