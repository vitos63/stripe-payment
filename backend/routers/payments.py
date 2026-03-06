from fastapi import APIRouter, Body, Depends, Request
from typing import Annotated

from ..services.product_service import ProductService
from ..services.payment_service import PaymentService
from ..dependencies import product_service, payment_service


router = APIRouter()


@router.post("/checkout/")
async def create_checkout_session(
    product_service: Annotated[ProductService, Depends(product_service)],
    payment_service: Annotated[PaymentService, Depends(payment_service)],
    product_id: int = Body(..., embed=True),
):
    product = await product_service.get_by_id(product_id=product_id)
    session = payment_service.create_checkout_session(product=product)
    return {"url": session.url}


@router.post("/webhook/")
async def stripe_webhook(
    request: Request, service: Annotated[PaymentService, Depends(payment_service)]
):
    return await service.handle_webhook(request=request)
