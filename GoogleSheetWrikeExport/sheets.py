
import os
from dotenv import load_dotenv
load_dotenv()

def write(data):
    import gspread
    configLocation = os.getenv('CONFIG_LOCATION')
    gc = gspread.service_account(configLocation)
    sh = gc.open("Tutorial").sheet1
    print(sh.get('b1'))
    formattedData = []
    for task in data:
        for row in task:
            formattedData.append([row,task[row]])
        
    sh.update("A1", formattedData)
    return "done"
