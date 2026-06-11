from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    SECRET_KEY = "dev"
    DATABASE = BASE_DIR / "instance" / "exam_results.sqlite3"
