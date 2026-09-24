import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "accounts.json"


def load_accounts():
    DATA_FILE.parent.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_accounts(accounts):
    DATA_FILE.parent.mkdir(exist_ok=True)

    temporary_file = DATA_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)

    temporary_file.replace(DATA_FILE)
