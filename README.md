# Testautomation – Loan Lab (Projektarbete Individuellt)

Individuellt projektarbete från FSH-kursen: ett testautomationsramverk under uppbyggnad för en fiktiv API-tjänst, "Loan Lab" (lånehantering).

## Teknikstack

- **Python** 3.11+
- **pytest** – test runner
- **requests** – API-anrop
- **Playwright** – förberedd för UI-tester
- **pydantic**, **faker**, **python-dotenv**

## Projektstruktur

```
src/loan_lab/
├── api/
│   └── client.py              # LoanLabApiClient – wrapper för API-anrop (GET/POST/PATCH/DELETE)
├── helpers/
│   └── skatteverket_testdata.py  # Hämtar testpersonnummer från Skatteverkets testdata-API
├── pages/                      # Page objects (förberett för UI-tester)
└── config.py                   # Miljökonfiguration (bas-URL, API-nycklar via .env)

tests/
└── conftest.py                 # Delade fixtures (api_client, skv_client m.fl.)
```

## Status

Grundstruktur, API-klient och fixtures är på plats. Testfallen är under utveckling.

## Installation

```bash
pip install -r requirements.txt
playwright install
```

Skapa en `.env`-fil i projektets rot med:

```
LOAN_LAB_API_BASE_URL=https://souderbroder-loan-lab.lovable.app
LOAN_LAB_API_KEY=<din-api-nyckel>
LOAN_LAB_ADMIN_API_KEY=<din-admin-api-nyckel>
```

## Köra testerna

```bash
pytest
```

Markörer för att köra specifika testtyper:

```bash
pytest -m api
pytest -m ui
```
