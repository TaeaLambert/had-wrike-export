import os
import google.auth


def google_crential_env_to_file():
    with open(os.getenv("CONFIG_LOCATION"), "w") as f:
        f.write(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))


def write_tasks(data):
    import gspread

    configLocation = os.getenv("CONFIG_LOCATION")
    gc = gspread.service_account(configLocation)
    sh = gc.open("H&D | Wrike Task Export | Working").worksheet("wrikeTaskoutput")
    sh.clear()
    sh.update("A1", data)
    return "done"

    # import gspread
    # configLocation = os.getenv('CONFIG_LOCATION')
    # gc = gspread.service_account(configLocation)
    # gc.import_csv("1KVgECuPo1-6FvjzZn-5Ex485173-Sz_l9cFIy8-mpDE", data)
    # return "done"


def write_folders(data):
    import gspread

    configLocation = os.getenv("CONFIG_LOCATION")
    gc = gspread.service_account(configLocation)
    sh = gc.open("H&D | Wrike Task Export | Working").worksheet("wrikeFolderoutput")
    sh.clear()
    sh.update("A1", data)
    return "done"

    # import gspread
    # configLocation = os.getenv('CONFIG_LOCATION')
    # gc = gspread.service_account(configLocation)
    # gc.import_csv("1KVgECuPo1-6FvjzZn-5Ex485173-Sz_l9cFIy8-mpDE", data)
    # return "done"
