
# from GoogleSheetWrikeExport.getTaskFromWrike import getWrikeTasks, writeToJson
import utils
import wrike
import sheets
import os
from dotenv import load_dotenv

load_dotenv()
wrikekey = os.getenv('WRIKE_KEY')
api_url = 'https://www.wrike.com/api/v4/tasks'
header = {'Authorization': 'Bearer ' + wrikekey}

def main():
    # get data from Wrike
    rawJson = wrike.get_tasks( api_url, header )
    # save data to json file
    utils.write_to_json(rawJson, './GoogleSheetWrikeExport/wrikeTasks.json')
    
    # need to format data for google sheet    
    
    # load data from json file
    json = utils.read_in_json('./GoogleSheetWrikeExport/wrikeTasks copy.json')
    # write data to Google Sheets
    print(sheets.write(json))
    
    
    
    
if __name__ == '__main__':
    main()