from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from ..repositories.product_repository import ProductRepo
from ..services.product_service import ProductService
from ..services.payment_service import PaymentService


class Container(containers.DeclarativeContainer):
    session = providers.Dependency(instance_of=AsyncSession)

    product_repository = providers.Factory(
        ProductRepo,
        session=session
    )

    product_service = providers.Factory(
        ProductService,
        product_repo=product_repository
    )

    payment_service = providers.Factory(
        PaymentService,
    )
