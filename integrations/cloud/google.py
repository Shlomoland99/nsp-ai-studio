import os
class GoogleAdapter:
    def __init__(self): self.api_key=os.getenv("GEMINI_API_KEY")
    def configured(self)->bool: return bool(self.api_key)
