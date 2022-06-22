import json
import csv
from pathlib import Path
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def write_to_json(data, path):
    # write data to a json file
    with open(path, "w") as outfile:
        json.dump(data, outfile)
    return "done"


def json_to_csv(json_path, csv_path):
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)


def csv_to_list(path: Path):
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

        # return [row for row in csv.reader(f)]


def relative_date(years: int = 0, months: int = 0, day: int = 0) -> datetime:
    """
    Args:
        years (int, optional): _description_. Defaults to 0.
        months (int, optional): _description_. Defaults to 0.
        day (int, optional): _description_. Defaults to 0.
    Returns:
        datetime: _description_
    """

    return datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + relativedelta(years, months, day)


def get_wrike_queary_dates(ahead: int = 6, past: int = 13) -> str:
    """
    This function takes the number of months ahead and the number of months past
    Both arguments are positive integers and default to 6 and 13 respectively
    """
    six_month_ahead = relative_date(months=ahead)
    thirteen_month_behind = relative_date(months=-past)
    return json.dumps(
        {
            "start": thirteen_month_behind.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "end": six_month_ahead.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    )
