
import os
from dotenv import load_dotenv

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
        
    
    
    
    # # write data to google sheet
    # sheet.append_row(data)
    return "done"

    
    
    
# googleSheetWrite({"receiver_email_1":6, "receiver_email_2":8, "receiver_email_3":10})