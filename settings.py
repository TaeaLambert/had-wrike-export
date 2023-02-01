import logging
import os
from pathlib import Path

TMP_FOLDER = Path("/tmp")

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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tmp/firebase-service-account.json"

else:
    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.setup_logging()


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
