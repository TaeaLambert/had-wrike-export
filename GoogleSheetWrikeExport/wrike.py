import os
import requests

class WrikeConfig:
    wrikekey = None
    api_url = 'https://www.wrike.com/api/v4/tasks?pageSize=1000&fields=["customFields"]'
    
    def __init__(self,  wrike_key = None) -> None:
        if not wrike_key:
            self.wrikekey = os.getenv('WRIKE_KEY')
        else:
            self.wrikekey = wrike_key
    
    def get_header(self):
        return {'Authorization': 'Bearer ' + self.wrikekey}


def get_tasks(wrike_config = None):
    if wrike_config is None:
        wrike_config = WrikeConfig()
    
    
    # http request to get all tasks in the Wrike account
    response = requests.get(wrike_config.api_url, headers=wrike_config.get_header())
    
    # print(response.json())
    response_json = response.json()
    print(response_json)
    response_array = response_json['data']
    while True:
        nextPageToken = response_json.get('nextPageToken')
        print(nextPageToken)
        if nextPageToken:
            response = requests.get(wrike_config.api_url + "&nextPageToken=" + nextPageToken, headers=wrike_config.get_header())
            response_json = response.json()
            response_array = response_array + response_json['data']
        else:
            break

    
    return response_array


