from flask import Flask, request, abort
import main

app = Flask(__name__)


@app.route("/googleSheetWrikeExport", methods=["POST"])
def defultRun():
    print("Running GoogleSheetWrikeExport...")
    if request.method == "POST":
        response = main.runGoogleSheetWrikeExport()
        if response == None:
            abort(400)
        else:
            return "success", 200
    else:
        abort(405)


if __name__ == "__main__":
    app.run()
