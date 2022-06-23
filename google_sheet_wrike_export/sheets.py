import os
import gspread
import google.auth
import google_sheet_wrike_export.config as config


def google_crential_env_to_file():
    with open(config.CONFIG_LOCATION, "w") as f:
        f.write(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))


def write_tasks(data):
    gc = gspread.service_account(config.CONFIG_LOCATION)
    sh = gc.open("H&D | Wrike Task Export | Working").worksheet("wrikeTaskoutput")
    sh.clear()
    sh.update("A1", data)
    return "done"


def write_folders(data):
    gc = gspread.service_account(config.CONFIG_LOCATION)
    sh = gc.open("H&D | Wrike Task Export | Working").worksheet("wrikeFolderoutput")
    sh.clear()
    sh.update("A1", data)
    return "done"
