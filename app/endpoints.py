import sqlalchemy.exc
from fastapi import APIRouter
from databases.postgres.crud import insert_note, show_notes
from app.models import Response


router = APIRouter()


@router.get('/')
async def main():
    return 'Hello user!'


@router.get('/note')
async def all_notes(user_id: int):
    try:
        return await show_notes(user_id=user_id)
    except sqlalchemy.exc.IntegrityError:
        return Response(**{"status": "error",
                           "message": "Ошибка вывода заметок, возможно такой person_id не существует",
                           "code": 400,
                           "data": locals()})


@router.post('/note')
async def new_note(header: str, text: str, user_id: int, tags: list | None = None):
    try:
        await insert_note(header=header, text=text, user_id=user_id, tags=tags)
        return f'Note inserted'
    except sqlalchemy.exc.IntegrityError:
        return Response(**{"status": "error",
                           "message": "Ошибка вставки заметки, возможно такой person_id не существует",
                           "code": 400,
                           "data": locals()})