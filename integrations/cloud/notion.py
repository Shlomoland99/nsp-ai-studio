import os
class NotionAdapter:
    def __init__(self): self.token=os.getenv("NOTION_API_TOKEN")
    def configured(self)->bool: return bool(self.token)
