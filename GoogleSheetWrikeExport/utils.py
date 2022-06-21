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


def get_wrike_queary_dates():
    six_month_ahead = datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + relativedelta(months=6)
    thirteen_month_behind = datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + relativedelta(months=-13)
    return (
        '{"start":"'
        + thirteen_month_behind.strftime("%Y-%m-%dT%H:%M:%SZ")
        + '","end":"'
        + six_month_ahead.strftime("%Y-%m-%dT%H:%M:%SZ")
        + '"}'
    )
