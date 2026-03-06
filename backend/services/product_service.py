from ..repositories.product_repository import ProductRepo
from ..database.products import Products


class ProductService:
    def __init__(self, product_repo: ProductRepo):
        self._product_repo = product_repo

    async def get_all_products(self) -> list[Products]:
        products = await self._product_repo.select_all()
        return products

    async def get_by_id(self, product_id: int) -> Products | None:
        product = await self._product_repo.select_by_id(product_id=product_id)
        return product

    async def create_product(self, title: str, price: int) -> Products:
        product = await self._product_repo.create_product(title=title, price=price)
        return product
