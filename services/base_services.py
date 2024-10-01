from sqlalchemy import select, insert, delete


from config.database import async_session_maker

class BaseService:
    model = None


    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            result = result.scalars().all()
            return result

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            return result

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            return result


    @classmethod
    async def add_data(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs)
            await session.execute(query)
            await session.commit()