from __future__ import annotations
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
    def __init__(self, api_base_url: str, timeout_s: float = 10.0):
        self.api_base_url = api_base_url.rstrip("/")
        self.timeout_s = timeout_s
        self.session = requests.Session()

        if settings.api_key:
            if settings.api_key_header.lower() == "authorization":
                self.session.headers.update({"Authorization": f"Bearer {settings.api_key}"})
            else:
                self.session.headers.update({settings.api_key_header: settings.api_key})

        self.session.headers.update({"Accept": "application/json"})

    def request(self, method: str, path: str, *, params: dict | None = None, json: Any | None = None, headers: dict | None = None) -> ApiResponse:
        url = self.api_base_url + path
        r = self.session.request(method=method, url=url, params=params, json=json, headers=headers, timeout=self.timeout_s)
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

    def get(self, path: str, **kwargs) -> ApiResponse:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> ApiResponse:
        return self.request("POST", path, **kwargs)
