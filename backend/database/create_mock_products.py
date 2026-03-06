import asyncio

from ..services.product_service import ProductService
from ..repositories.product_repository import ProductRepo
from ..dependencies import db_session


async def create_mock_products():
    session = await db_session()
    product_service = ProductService(product_repo=ProductRepo(session=session))
    await product_service.create_product(title="Product 1", price=10)
    await product_service.create_product(title="Product 2", price=20)
    await product_service.create_product(title="Product 3", price=30)
    await session.commit()
    await session.close()


if __name__ == "__main__":
    asyncio.run(create_mock_products())
