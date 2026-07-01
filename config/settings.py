import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KAFKA_BROKER = os.getenv("KAFKA_BROKER")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

settings = Settings()
