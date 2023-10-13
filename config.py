import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your-secret-key"
    FIREBASE_CONFIG = "firebase_credentials.json"
