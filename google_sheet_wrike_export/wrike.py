import os
import requests
from google_sheet_wrike_export import utils


class WrikeConfig:
    wrikekey = None
    get_tasks_url = (
        "https://www.wrike.com/api/v4/tasks?pageSize=1000&fields="
        '["customFields","superTaskIds","superParentIds","parentIds"]'
    )
    get_folders_url = "https://www.wrike.com/api/v4/folders"

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
    wrike_config.add_params("&updatedDate=" + utils.get_wrike_queary_dates())
    print(wrike_config.get_tasks_url)
    response = requests.get(
        wrike_config.get_tasks_url, headers=wrike_config.get_header()
    )
    response_json = response.json()
    print(response.json())
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
