import settings
import os
import psutil
import uvicorn


from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse


from program.function import (
    run_google_sheet_wrike_export,
)  # , run_mongodb_export, write_hubspot_products_to_google_sheet


app = FastAPI()


@app.get("/")
def index():
    print("get request on index")
    return JSONResponse(
        "[had-wrike-google-sheet-export] is running\n"
        + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2))
        + " MB"
    )


@app.get("/debug-sentry")
def crash():
    print(1 / 0)
    raise HTTPException(status.HTTP_418_IM_A_TEAPOT, "crash")


@app.post("/write_wrike_to_google_sheets")
def write_wrike_to_google_sheets(request: Request):
    print("Running run_google_sheet_wrike_export...")
    if request.method == "POST":
        response = run_google_sheet_wrike_export()
        if response is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Somthing went wrong")
        else:
            return JSONResponse("Success")
    else:
        raise HTTPException(status.HTTP_405_METHOD_NOT_ALLOWED, "This Method is not allowed")


# @app.route("/mongodb_export", methods=["POST"])
# def mongodb_export():
#     print("Running mongodb_export...")
#     if request.method == "POST":
#         response = run_mongodb_export()
#         if response is None:
#             abort(400)
#         else:
#             return "success", 200
#     else:
#         abort(405)


# @app.route("/write_products_to_google_sheet", methods=["POST"])
# def run():
#     print("Running write_products_to_google_sheet...")
#     if request.method == "POST":
#         response = write_hubspot_products_to_google_sheet()
#         if response is None:
#             abort(400)
#         else:
#             return "success", 200
#     else:
#         abort(405)


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=os.getenv("PORT"), reload=True, workers=1)
