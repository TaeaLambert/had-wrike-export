import os
from flask import Flask, request, abort
from google_sheet_wrike_export.function import run_google_sheet_wrike_export
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("FLASK_DEBUG")
    )
