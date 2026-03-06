from fastapi import Request, HTTPException
import stripe
from stripe.checkout import Session

from ..config import STRIPE_WEBHOOK, FRONTEND_URL
from ..database import Products


class PaymentService:
    async def handle_webhook(self, request: Request):
        payload = await request.body()
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK
            )

        except stripe.error.SignatureVerificationError:
            raise HTTPException(status_code=400, detail="Invalid signature")

        if event.get('type') == "checkout.session.completed":
            return {"status": 'Completed session'}

    def create_checkout_session(self, product: Products) -> Session:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product.title,
                        },
                        "unit_amount": product.price * 100,
                    },
                    "quantity": 1,
                    "adjustable_quantity": {
                        "enabled": True,
                    },
                }
            ],
            customer_email='abc@gmail.com',
            mode="payment",
            success_url=FRONTEND_URL + "/success/",
            cancel_url=FRONTEND_URL,
        )
        return checkout_session
