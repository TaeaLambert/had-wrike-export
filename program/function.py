import os
import psutil
from pathlib import Path
from program.utils import wrike, sheets, files
from program.utils.products import create_csv_and_convert_to_list, format_products
from program.utils.sheets import google_crential_env_to_file, write_to_google_sheet
from program.api_requests import (
    get_all_product_properties,
    get_all_products,
)
from program.utils.mongodb import (
    get_all_collections_mongodb,
    get_all_portal_ids_in_collection,
)

# MICRO APPS:
def run_mongodb_export():
    print("Running mongodb_export...")
    list_of_collections = get_all_collections_mongodb()
    json_holder = {}
    collection_max_length = 0

    for collection in list_of_collections:
        print(collection)
        portal_ids = get_all_portal_ids_in_collection(collection)
        if len(portal_ids) > collection_max_length:
            collection_max_length = len(portal_ids)
        json_holder[collection] = portal_ids
    for portal_ids in json_holder.values():
        while len(portal_ids) < collection_max_length:
            portal_ids.append("")

    folder_path = Path("./CSV")
    files.write_to_json(json_holder, folder_path / "mongodb_export.json")
    files.json_to_csv(folder_path / "mongodb_export.json", folder_path / "mongodb_export.csv")
    google_crential_env_to_file()
    write_to_google_sheet(
        files.csv_to_list(folder_path / "mongodb_export.csv"),
        os.getenv("MICROAPP_FILE"),
        os.getenv("MICROAPP_SHEET"),
    )
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del list_of_collections
    del json_holder
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    return "success", 200


# WRIKE:
def run_google_sheet_wrike_export():
    google_crential_env_to_file()
    folder_path = Path("./CSV")
    task_csv_path = Path(folder_path / "wrikeTasks.csv")
    task_formatted_csv_path = Path(folder_path / "wrikeTasks_formatted.csv")
    folder_csv_path = Path(folder_path / "wrikeFolder.csv")
    project_csv_path = Path(folder_path / "wrikeProject.csv")
    contact_csv_path = Path(folder_path / "wrikeContact.csv")
    workflow_csv_path = Path(folder_path / "wrikeWorkflow.csv")

    print("Getting data from Wrike...")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    wrike_task = wrike.get_tasks()
    wrike_task_unformatted_array = wrike_task[0]
    wrike_task_formatted_array = wrike_task[1]
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_task
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")

    # get data from Wrike
    files.write_to_json(wrike_task_unformatted_array, folder_path / "wrikeTasks.json")
    files.write_to_json(wrike_task_formatted_array, folder_path / "wrikeTasks_formatted.json")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_task_unformatted_array
    del wrike_task_formatted_array
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    print("Tasks loaded & saved")

    wrike_folder_array = wrike.get_folders()
    files.write_to_json(wrike_folder_array, folder_path / "wrikeFolders.json")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_folder_array
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    print("Folders loaded & saved")

    wrike_folder_array = wrike.get_projects()
    files.write_to_json(wrike_folder_array, folder_path / "wrikeProjects.json")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_folder_array
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    print("Folders loaded & saved")

    wrike_contacts_array = wrike.get_contacts()
    files.write_to_json(wrike_contacts_array, folder_path / "wrikeContacts.json")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_contacts_array
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    print("Contacts loaded & saved")

    wrike_workflows_array = wrike.get_workflows()
    files.write_to_json(wrike_workflows_array, folder_path / "wrikeWorkflows.json")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del wrike_workflows_array
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    print("Workflows loaded & saved")

    files.json_to_csv(folder_path / "wrikeTasks.json", task_csv_path)
    files.json_to_csv(folder_path / "wrikeTasks_formatted.json", task_formatted_csv_path)
    files.json_to_csv(folder_path / "wrikeFolders.json", folder_csv_path)
    files.json_to_csv(folder_path / "wrikeProjects.json", project_csv_path)
    files.json_to_csv(folder_path / "wrikeContacts.json", contact_csv_path)
    files.json_to_csv(folder_path / "wrikeWorkflows.json", workflow_csv_path)

    # load data from json file
    csv_list = files.csv_to_list(task_csv_path)
    csv_list_formatted = files.csv_to_list(task_formatted_csv_path)
    folder_list = files.csv_to_list(folder_csv_path)
    project_list = files.csv_to_list(project_csv_path)
    contact_list = files.csv_to_list(contact_csv_path)
    workflow_list = files.csv_to_list(workflow_csv_path)

    sheets.google_crential_env_to_file()
    print("Writing data to Google Sheets...")
    sheets.write_workflow(workflow_list)
    print("Workflows written")
    sheets.write_folders(folder_list)
    print("Folders written")
    sheets.write_projects(project_list)
    print("Projects written")
    sheets.write_contacts(contact_list)
    print("Contacts written")
    sheets.write_tasks(csv_list)
    print("Tasks written")
    sheets.write_tasks_formatted(csv_list_formatted)
    print("Tasks_formatted written")
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del csv_list_formatted
    del csv_list
    del folder_list
    del project_list
    del contact_list
    del workflow_list
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    return "Completed", 200


# PRODUCTS:
def write_products_to_google_sheet():
    print("post request on run_main")
    properties = get_all_product_properties()
    products = get_all_products(properties)
    results = format_products(products)
    JSON_FILE = "./CSV/products.json"
    CSV_FILE = "./CSV/products.csv"
    list_for_google_sheets = create_csv_and_convert_to_list(JSON_FILE, CSV_FILE, results)
    google_crential_env_to_file()
    write_to_google_sheet(list_for_google_sheets, os.getenv("GOOGLE_WORKBOOK"), os.getenv("GOOGLE_SHEET"))
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    del properties
    del products
    del results
    del list_for_google_sheets
    print("RAM memory used:\t" + str(round(psutil.Process().memory_info().rss / (1024 * 1024), 2)) + " MB")
    return "completed", 200
