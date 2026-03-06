from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import stripe

from .config import FRONTEND_URL, STRIPE_SECRET_KEY
from .routers.products import router as product_router
from .routers.payments import router as payment_router


origins = [
    FRONTEND_URL,
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
stripe.api_key = STRIPE_SECRET_KEY

app.include_router(product_router)
app.include_router(payment_router)
