import pytest

from loan_lab.config import settings
from loan_lab.api.client import LoanLabApiClient
from loan_lab.helpers.skatteverket_testdata import SkatteverketTestdataClient, extract_personnummer

@pytest.fixture(scope="session")
def api_client() -> LoanLabApiClient:
    return LoanLabApiClient(settings.api_base_url)

@pytest.fixture(scope="session")
def skv_client() -> SkatteverketTestdataClient:
    return SkatteverketTestdataClient()

@pytest.fixture()
def skv_personnummer_list(skv_client) -> list[str]:
    resp = skv_client.get_test_personnummer(limit=10, offset=0)
    assert resp.status_code == 200
    return extract_personnummer(resp.json)
