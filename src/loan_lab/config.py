from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("LOAN_LAB_BASE_URL", "https://souderbroder-loan-lab.lovable.app")
    api_base_url: str = os.getenv("LOAN_LAB_API_BASE_URL", "https://souderbroder-loan-lab.lovable.app")
    api_key: str | None = os.getenv("LOAN_LAB_API_KEY")
    api_key_header: str = os.getenv("LOAN_LAB_API_KEY_HEADER", "Authorization")  # Standard är "Authorization"

settings = Settings()
