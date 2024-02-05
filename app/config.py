import os
from dotenv import load_dotenv


class Settings():
    load_dotenv()
    database_url: str = os.getenv("DB_URL")


settings = Settings()
