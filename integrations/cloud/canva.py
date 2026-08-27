import os
class CanvaAdapter:
    def __init__(self): self.token=os.getenv("CANVA_API_TOKEN")
    def configured(self)->bool: return bool(self.token)
