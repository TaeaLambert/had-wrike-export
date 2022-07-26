import os
import requests
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


class WrikeConfig:
    wrikekey = None
    get_tasks_url = (
        "https://www.wrike.com/api/v4/tasks?pageSize=1000&fields="
        '["customFields","superTaskIds","superParentIds","parentIds"]'
    )
    get_folders_url = "https://www.wrike.com/api/v4/folders"

    get_contacts_url = "https://www.wrike.com/api/v4/contacts"

    get_workflow_url = "https://www.wrike.com/api/v4/workflows"

    def __init__(self, wrike_key=None) -> None:
        if not wrike_key:
            self.wrikekey = os.getenv("WRIKE_KEY")
        else:
            self.wrikekey = wrike_key

    def get_header(self):
        return {"Authorization": "Bearer " + self.wrikekey}

    def add_params(self, params):
        self.get_tasks_url += params


def get_tasks(wrike_config=None):
    if wrike_config is None:
        wrike_config = WrikeConfig()
    wrike_config.add_params("&updatedDate=" + get_wrike_queary_dates())
    print(wrike_config.get_tasks_url)
    response = requests.get(
        wrike_config.get_tasks_url, headers=wrike_config.get_header()
    )
    response_json = response.json()
    # print(response.json())
    response_array = response_json["data"]
    i = 1000
    while True:
        next_page_token = response_json.get("nextPageToken")
        print(str(i) + " tasks loaded")
        if next_page_token:
            response = requests.get(
                wrike_config.get_tasks_url + "&nextPageToken=" + next_page_token,
                headers=wrike_config.get_header(),
            )
            response_json = response.json()
            response_array = response_array + response_json["data"]
            i += 1000
        else:
            break

    return response_array


def get_folders(wrike_config=None):
    if wrike_config is None:
        wrike_config = WrikeConfig()

    response = requests.get(
        wrike_config.get_folders_url, headers=wrike_config.get_header()
    )
    folder_json = response.json()["data"]
    response_array = []
    for folder in folder_json:
        # ['IEACTPDZI4NOQZLA']
        response_array.append(
            {
                "parent folder id": "['" + folder["id"] + "']",
                "folder title": folder["title"],
            }
        )
    return response_array


def get_workflows(wrike_config=None):
    if wrike_config is None:
        wrike_config = WrikeConfig()

    response = requests.get(
        wrike_config.get_workflow_url, headers=wrike_config.get_header()
    )
    folder_json = response.json()
    response_array = []
    for response in folder_json.get("data"):
        for items in response["customStatuses"]:
            dict = {}
            dict["id"] = items["id"]
            dict["satus"] = items["name"]
            dict["workflow Type"] = response["name"]
            response_array.append(dict)
    return response_array


def get_contacts(wrike_config=None):
    if wrike_config is None:
        wrike_config = WrikeConfig()

    response = requests.get(
        wrike_config.get_contacts_url, headers=wrike_config.get_header()
    )
    contact_json = response.json()["data"]
    response_array = []
    for contact in contact_json:
        contact_ids = contact["profiles"][0]
        contact_id = contact_ids["accountId"]
        f_name = "unkown"
        l_name = "name"
        if "firstName" in contact:
            f_name = contact["firstName"]

        if "lastName" in contact:
            l_name = contact["lastName"]

        # ['IEACTPDZI4NOQZLA']
        response_array.append(
            {
                "Contact ID": contact_id,
                "Name": f_name + " " + l_name,
            }
        )
    return response_array


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
