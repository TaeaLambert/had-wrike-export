import os
from flask import Flask, request, abort
from GoogleSheetWrikeExport.function import *
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/googleSheetWrikeExport", methods=["POST"])
def defultRun():
    print("Running GoogleSheetWrikeExport...")
    if request.method == "POST":
        response = runGoogleSheetWrikeExport()
        if response == None:
            abort(400)
        else:
            return "success", 200
    else:
        abort(405)


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
