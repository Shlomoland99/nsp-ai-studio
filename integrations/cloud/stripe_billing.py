import os
class StripeBilling:
    def __init__(self):
        self.secret_key=os.getenv("STRIPE_SECRET_KEY")
    def configured(self)->bool: return bool(self.secret_key)
    def checkout_url(self,price_id:str,success_url:str,cancel_url:str)->str:
        if not self.configured(): raise RuntimeError("STRIPE_SECRET_KEY is not configured")
        raise NotImplementedError("Create Stripe Checkout Session in the deployment service.")