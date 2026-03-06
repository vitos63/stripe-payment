from fastapi import Depends, APIRouter
from typing import Annotated

from ..services.product_service import ProductService
from ..dependencies import product_service


router = APIRouter()


@router.get("/get-all-products/")
async def get_all_products(service: Annotated[ProductService,
                                              Depends(product_service)]):
    result = await service.get_all_products()
    return result
