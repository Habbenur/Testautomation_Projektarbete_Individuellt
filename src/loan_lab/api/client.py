from dataclasses import dataclass
from typing import Any, Optional
import requests

from loan_lab.config import settings


@dataclass
class ApiResponse:
    status_code: int
    headers: dict[str, str]
    json: Optional[Any]
    text: str


class LoanLabApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _get_headers(self, admin: bool = False) -> dict:
        key = settings.admin_api_key if admin else settings.api_key

        if not key:
            raise RuntimeError("API key missing in .env")

        return {"x-api-key": key}

    def request(self, method: str, path: str, *, json=None, params=None, admin=False):
        url = self.base_url + path

        r = self.session.request(
            method=method,
            url=url,
            json=json,
            params=params,
            headers=self._get_headers(admin=admin),
            timeout=10,
        )

        try:
            payload = r.json()
        except Exception:
            payload = None

        return ApiResponse(
            status_code=r.status_code,
            headers=dict(r.headers),
            json=payload,
            text=r.text,
        )

    def get(self, path: str, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs):
        return self.request("POST", path, **kwargs)

    def patch(self, path: str, **kwargs):
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.request("DELETE", path, **kwargs)
