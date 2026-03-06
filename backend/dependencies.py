from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .services.product_service import ProductService
from .services.payment_service import PaymentService
from .di.container import Container
from .database.engine import AsyncSessionFactory


async def db_session() -> AsyncSession:
    async with AsyncSessionFactory() as db_connection:
        return db_connection


async def container(session: Annotated[AsyncSession, Depends(db_session)]) -> Container:
    return Container(session=session)


async def product_service(container_: Annotated[Container, Depends(container)]) -> ProductService:
    return container_.product_service()


async def payment_service(container_: Annotated[Container, Depends(container)]) -> PaymentService:
    return container_.payment_service()
