from google_sheet_wrike_export import utils, wrike, sheets
from pathlib import Path


def run_google_sheet_wrike_export():

    folder_path = Path("./google_sheet_wrike_export")
    task_csv_path = Path(folder_path / "wrikeTasks.csv")
    folder_csv_path = Path(folder_path / "wrikeFolder.csv")
    contact_csv_path = Path(folder_path / "wrikeContact.csv")
    workflow_csv_path = Path(folder_path / "wrikeWorkflow.csv")

    # get data from Wrike
    print("Getting data from Wrike...")
    wrike_task_array = wrike.get_tasks()
    print("Tasks loaded")
    wrike_folder_array = wrike.get_folders()
    print("Folders loaded")
    wrike_contacts_array = wrike.get_contacts()
    print("Contacts loaded")
    wrike_workflows_array = wrike.get_workflows()

    # save data to json file
    utils.write_to_json(wrike_task_array, folder_path / "wrikeTasks.json")
    # save data to json file
    utils.write_to_json(wrike_folder_array, folder_path / "wrikeFolders.json")
    # save data to json file
    utils.write_to_json(wrike_contacts_array, folder_path / "wrikeContacts.json")
    # save data to json file
    utils.write_to_json(wrike_workflows_array, folder_path / "wrikeWorkflows.json")

    # format data in a way that i can use it in Google Sheets
    utils.json_to_csv(folder_path / "wrikeTasks.json", task_csv_path)
    utils.json_to_csv(folder_path / "wrikeFolders.json", folder_csv_path)
    utils.json_to_csv(folder_path / "wrikeContacts.json", contact_csv_path)
    utils.json_to_csv(folder_path / "wrikeWorkflows.json", workflow_csv_path)

    # # load data from json file
    csv_list = utils.csv_to_list(task_csv_path)
    folder_list = utils.csv_to_list(folder_csv_path)
    contact_list = utils.csv_to_list(contact_csv_path)
    workflow_list = utils.csv_to_list(workflow_csv_path)

    sheets.google_crential_env_to_file()
    print("Writing data to Google Sheets...")
    sheets.write_workflow(workflow_list)
    print("Workflows written")
    sheets.write_folders(folder_list)
    print("Folders written")
    sheets.write_contacts(contact_list)
    print("Contacts written")
    sheets.write_tasks(csv_list)
    print("Tasks written")
    print("Done!")
    return "success"
