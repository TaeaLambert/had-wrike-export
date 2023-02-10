import os
from pathlib import Path

from program.utils.files.files_managment_pandas import json_to_csv
from program.utils.files.files_managment import csv_to_list, write_to_json
from program.utils.wrike.wrike_api import get_contacts_v2, get_tasks_due_date
from program.utils.google_sheets.google_sheets import google_sheets


# WRIKE:
def run_google_sheet_wrike_export():
    folder_path = Path("./CSV")
    csv_task_formatted_path = Path(folder_path / "wrikeTasks_formatted.csv")
    csv_contacts_path = Path(folder_path / "wrike_userid_and_name.csv")

    print("Getting data from Wrike...")
    write_to_json(get_tasks_due_date(), folder_path / "wrikeTasks_formatted.json")
    json_to_csv(folder_path / "wrikeTasks_formatted.json", csv_task_formatted_path)
    csv_list_formatted = csv_to_list(csv_task_formatted_path)
    google_sheet_client = google_sheets()
    google_sheet_client.set_csv_into_sheet(
        "H&D | Resource Management | Proposal | Working",
        "Wrike Task dueDate -7<>+365 days",
        csv_list_formatted,
        "A1",
        True,
        3,
        "asc",
        "A2:Q50000",
    )
    del csv_list_formatted

    write_to_json(get_contacts_v2(), folder_path / "wrike_userid_and_name.json")
    json_to_csv(folder_path / "wrike_userid_and_name.json", csv_contacts_path)
    csv_contacts = csv_to_list(csv_contacts_path)
    google_sheet_client = google_sheets()
    google_sheet_client.set_csv_into_sheet(
        "H&D | Resource Management | Proposal | Working",
        "User ID & User Name",
        csv_contacts,
        "A1",
        True,
        3,
        "asc",
        "A2:Q50000",
    )
    del csv_contacts

    return "Completed", 200
