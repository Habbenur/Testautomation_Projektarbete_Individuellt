from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    api_base_url: str = os.getenv(
        "LOAN_LAB_API_BASE_URL",
        "https://souderbroder-loan-lab.lovable.app"
    )

    api_key: str | None = os.getenv("LOAN_LAB_API_KEY")
    admin_api_key: str | None = os.getenv("LOAN_LAB_ADMIN_API_KEY")

settings = Settings()
