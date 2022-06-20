import requests

def get_tasks(api_url, headers):
    # http request to get all tasks in the Wrike account
    response = requests.get(api_url, headers=headers)
    # print(response.json())
    return response.json()


