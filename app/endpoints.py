import sqlalchemy.exc
from fastapi import APIRouter
from databases.postgres.crud import insert_note
from app.models import Response
router = APIRouter()
import traceback

@router.get('/')
async def main():
    return 'Hello user!'


@router.post('/note')
async def new_note(header: str, text: str, person_id: int):
    try:
        await insert_note(header=header, text=text, person_id=person_id)
        return f'Note inserted'
    except sqlalchemy.exc.IntegrityError:
        return Response(**{"status": "error",
                           "message": "Ошибка вставки заметки, возможно такой person_id",
                           "code": 400,
                           "data": locals()})