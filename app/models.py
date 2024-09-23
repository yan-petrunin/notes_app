from pydantic import BaseModel, Field


class Response(BaseModel):
    status: str = Field(title="Статус ответа")
    message: str = Field(title="Ответ сервера")
    code: int = Field(title="Код ответа")
    data: dict | None = Field(title="Дополнительная информация", default=None)