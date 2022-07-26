import logging
import os
from flask import Flask
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from flask import Flask, request, abort
from program.function import (
    run_google_sheet_wrike_export,
    run_mongodb_export,
    write_products_to_google_sheet,
)
from dotenv import load_dotenv


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)

load_dotenv()

app = Flask(__name__)
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[
        FlaskIntegration(),
        sentry_logging,
    ],
    environment=os.getenv("FLASK_ENV", "development"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


@app.route("/", methods=["GET"])
def index():
    print("in index")
    return "[had-wrike-google-sheet-export] is running", 200


@app.route("/googleSheetWrikeExport", methods=["POST"])
def default_run():
    print("Running run_google_sheet_wrike_export...")
    if request.method == "POST":
        response = run_google_sheet_wrike_export()
        if response is None:
            abort(400)
        else:
            return "success", 200
    else:
        abort(405)


@app.route("/mongodb_export", methods=["POST"])
def mongodb_export():
    if request.method == "POST":
        response = run_mongodb_export()
        if response is None:
            abort(400)
        else:
            return "success", 200
    else:
        abort(405)


@app.route("/write_products_to_google_sheet", methods=["POST"])
def run():
    if request.method == "POST":
        response = write_products_to_google_sheet()
        if response is None:
            abort(400)
        else:
            return "success", 200
    else:
        abort(405)


if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("FLASK_DEBUG")
    )
