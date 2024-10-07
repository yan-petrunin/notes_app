from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
Base = declarative_base()


class Note(Base):
    __tablename__ = 'notes'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    header = mapped_column(String, nullable=False)
    text = mapped_column(String, nullable=False)
    creation_date = mapped_column(DateTime,  nullable=False)
    modify_date = mapped_column(DateTime,  nullable=False)
    user_id = mapped_column(ForeignKey('users.id'),  nullable=False)


class Tag(Base):
    __tablename__ = 'tags_list'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False, unique=True)


class NoteTag(Base):
    __tablename__ = 'note_tags'

    id = mapped_column(Integer, primary_key=True)
    note_id = mapped_column(ForeignKey('notes.id'),  nullable=False)
    tag_id = mapped_column(ForeignKey('tags_list.id'),  nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    password = mapped_column(String, nullable=False)


async def main():
    engine = create_async_engine(os.getenv('DATABASE_URL'), echo=True)
    AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with AsyncSession() as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(main())
