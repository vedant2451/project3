from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

DB_URL = os.environ.get("DB_URL")