import os
from sqlalchemy import Select, Insert
from databases.postgres.models import *
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncio
import datetime
from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(os.getenv('DATABASE_URL'), echo=True)
AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)


async def insert_note(header: str, text: str, user_id: int):
    async with AsyncSession() as session:
        note = Note(header=header, text=text,
                    creation_date=datetime.datetime.now(),
                    modify_date=datetime.datetime.now(),
                    user_id=user_id)
        session.add(note)
        await session.commit()


async def insert_user(username: str, email: str, password: str):
    async with AsyncSession() as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        await session.commit()

if __name__ == '__main__':
    #asyncio.run(insert_user('yan', 'yan@email.com', '12qwer'))
    asyncio.run(insert_note(header='zxcv', text='vcxz', user_id=2))
