import utils
import wrike
import sheets
from pathlib import Path


def runGoogleSheetWrikeExport():
    folder_path = Path("./GoogleSheetWrikeExport")
    task_csv_path = Path(folder_path / "wrikeTasks.csv")
    folder_csv_path = Path(folder_path / "wrikeFolder.csv")

    # get data from Wrike
    print("Getting data from Wrike...")
    wrike_task_array = wrike.get_tasks()
    print("Tasks loaded")
    wrike_folder_array = wrike.get_folders()
    print("Folders loaded")

    # save data to json file
    utils.write_to_json(wrike_task_array, folder_path / "wrikeTasks.json")
    # save data to json file
    utils.write_to_json(wrike_folder_array, folder_path / "wrikeFolders.json")

    # format data in a way that i can use it in Google Sheets
    utils.json_to_csv(folder_path / "wrikeTasks.json", task_csv_path)
    utils.json_to_csv(folder_path / "wrikeFolders.json", folder_csv_path)

    # # load data from json file
    csv_list = utils.csv_to_list(task_csv_path)
    folder_list = utils.csv_to_list(folder_csv_path)

    print("Writing data to Google Sheets...")
    sheets.write_tasks(csv_list)
    print("Tasks written")
    sheets.write_folders(folder_list)
    print("Folders written")
    print("Done!")
    return "success"
