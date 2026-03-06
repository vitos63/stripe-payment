from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import Products


class ProductRepo:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def select_all(self) -> list[Products]:
        stmt = (
            select(Products)
        )
        result = await self._session.execute(stmt)
        return list(result.scalars().all())

    async def select_by_id(self, product_id: int) -> Products | None:
        stmt = (
            select(Products).
            where(Products.id == product_id)
        )
        result = await self._session.execute(stmt)
        return result.scalars().one_or_none()

    async def create_product(self, title: str, price: int) -> Products:
        product = Products(title=title, price=price)
        self._session.add(product)
        await self._session.commit()
        await self._session.refresh(product)
        return product
