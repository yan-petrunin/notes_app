from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, declarative_base

Base = declarative_base()

class Notes(Base):
    __tablename__ = 'notes'

    id = mapped_column(Integer, primary_key=True, unique=True)
    header = mapped_column(String)
    text = mapped_column(String)
    creation_date = mapped_column(DateTime)
    modify_date = mapped_column(DateTime)
    person_id = mapped_column(Integer, unique=True)

class Tags(Base):
    __tablename__ = 'tags'

    id = mapped_column(Integer, primary_key=True)
    note_id = mapped_column(ForeignKey('notes.id'))
    tag = mapped_column(String)

class Persons(Base):
    __tablename__ = 'persons'

    id = mapped_column(Integer, primary_key=True)
    notes_id = mapped_column(ForeignKey('notes.id'))
    person_id = mapped_column(ForeignKey('notes.person_id'))