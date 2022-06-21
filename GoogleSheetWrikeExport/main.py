

# from GoogleSheetWrikeExport.getTaskFromWrike import getWrikeTasks, writeToJson
import utils
import wrike
import sheets
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()



def main():
    folder_path = Path("./GoogleSheetWrikeExport")
    task_path = Path(folder_path / "wrikeTasks.csv")
    
    # get data from Wrike
    # rawJson = wrike.get_tasks()
    
    # # save data to json file
    # utils.write_to_json(rawJson, folder_path / "wrikeTasks.json")
    

    # # format data in a way that i can use it in Google Sheets
    # utils.json_to_csv(folder_path / "wrikeTasks.json", task_path)   
    
    
    # # load data from json file
    csv_list = utils.csv_to_list(task_path)
   
    sheets.write(csv_list)
    
    
    
    
if __name__ == '__main__':
    main()