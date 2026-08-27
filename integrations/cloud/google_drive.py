import os
class GoogleDriveAdapter:
    def __init__(self): self.credentials=os.getenv("GOOGLE_DRIVE_CREDENTIALS_JSON")
    def configured(self)->bool: return bool(self.credentials)
