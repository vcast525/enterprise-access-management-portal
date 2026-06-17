import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.database.database import (
    DATABASE_PATH,
    initialize_database,
)


initialize_database()

print(f"Database created at: {DATABASE_PATH}")
print(f"Database exists: {DATABASE_PATH.exists()}")