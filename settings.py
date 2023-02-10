import os
import gspread
import logging
import google.auth
from pathlib import Path
from google.oauth2.service_account import Credentials

TMP_FOLDER = Path("/tmp")
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]


if os.getenv("RUNTIME") != "DOCKER":
    from dotenv import load_dotenv

    load_dotenv()
    if os.getenv("FLASK_ENV") == "production":
        logging.basicConfig(
            format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d:%H:%M:%S",
            level=logging.DEBUG,
        )

    TMP_FOLDER = Path("./tmp")
    TMP_FOLDER.mkdir(exist_ok=True)
    credentials = Credentials.from_service_account_file((TMP_FOLDER / "./service_account.json"), scopes=scopes)

else:
    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.setup_logging()
    credentials, project_id = google.auth.default(scopes=scopes)

gc = gspread.authorize(credentials)


import sentry_sdk

if os.getenv("FLASK_ENV") == "production":
    sentry_env = "production"
else:
    sentry_env = "development"
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    environment=sentry_env,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)
