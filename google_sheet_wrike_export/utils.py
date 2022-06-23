import json
import csv
from pathlib import Path
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def write_to_json(data, path):
    # write data to a json file
    with open(path, "w", encoding="utf8") as outfile:
        json.dump(data, outfile)
    return "done"


def json_to_csv(json_path, csv_path):
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)


def csv_to_list(path: Path):
    # with open("./google_sheet_wrike_export/wrikeTasks.json", "r") as csv_file:
    #     reader = csv.reader(csv_file)
    #     return list(reader)
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)


def relative_date(years: int = 0, months: int = 0, day: int = 0) -> datetime:

    return datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + relativedelta(years=years, months=months, days=day)


def get_wrike_queary_dates(ahead: int = 6, past: int = 13) -> str:
    """
    This function takes the number of months ahead and the number of months past
    Both arguments are positive integers and default to 6 and 13 respectively
    """
    print("Getting Wrike query dates...")
    print("Ahead:", ahead)
    print("Past:", past)
    six_month_ahead = relative_date(months=ahead)
    thirteen_month_behind = relative_date(months=-past)

    print(six_month_ahead)
    print(thirteen_month_behind)
    return json.dumps(
        {
            "start": thirteen_month_behind.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "end": six_month_ahead.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    )
