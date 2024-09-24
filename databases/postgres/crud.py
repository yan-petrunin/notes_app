from databases.postgres.models import *
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncio
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
import datetime
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

engine = create_async_engine(os.getenv('DATABASE_URL'), echo=True)
AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)


async def insert_note(header: str, text: str, user_id: int, tags: Optional[list] = None):
    async with AsyncSession() as session:
        note = Note(header=header, text=text,
                    creation_date=datetime.datetime.now(),
                    modify_date=datetime.datetime.now(),
                    user_id=user_id)
        if tags:
            params = [{"name": tag} for tag in tags]
            await session.execute(insert(Tag).values(params).on_conflict_do_nothing())
        session.add(note)
        await session.commit()


async def update_note(header: Optional[str] = None, text: Optional[str] = None, tags: Optional[list] = None):
    pass


async def show_notes(user_id: int):
    async with AsyncSession() as session:
        query = select(Note).where(Note.user_id == user_id)
        notes = await session.execute(query)
        return [note.__dict__ for note in notes.scalars().all()]


async def insert_user(username: str, email: str, password: str):
    async with AsyncSession() as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        await session.commit()

if __name__ == '__main__':
    #asyncio.run(insert_user('yan', 'yan@email.com', '12qwer'))
    #asyncio.run(insert_note(header='zxcv', text='vcxz', user_id=2))
    asyncio.run(show_notes(1))