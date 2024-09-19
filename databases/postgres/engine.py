from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from models import Base
import asyncio

async def main():
    # Создаем асинхронный движок для соединения с PostgreSQL через asyncpg
    engine = create_async_engine('postgresql+asyncpg://wcdb:wcdbpassword@localhost:5432/wcdb', echo=True)

    # Создаем асинхронный sessionmaker для работы с сессиями
    AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)

    # Создаем сессию
    async with AsyncSession() as session:
        # Создаем все таблицы, определенные в моделях
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # Закрываем движок после завершения работы
    await engine.dispose()

if __name__ == '__main__':
    asyncio.run(main())
