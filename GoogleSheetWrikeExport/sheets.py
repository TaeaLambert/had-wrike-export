
import os


def write(data):
    import gspread
    configLocation = os.getenv('CONFIG_LOCATION')
    gc = gspread.service_account(configLocation)
    sh = gc.open("H&D | Automated Wrike Task Reporting").sheet1
    sh.clear()
    print(sh.get('b1'))
    sh.update("A1", data)
    return "done"

    # import gspread
    # configLocation = os.getenv('CONFIG_LOCATION')
    # gc = gspread.service_account(configLocation)
    # gc.import_csv("1KVgECuPo1-6FvjzZn-5Ex485173-Sz_l9cFIy8-mpDE", data)
    # return "done"
