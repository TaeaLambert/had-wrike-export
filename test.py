json = {
    "id": "KUALHUF6",
    "type": "Person",
    "profiles": [{"accountId": "IEACTPDZ"}],
    "avatarUrl": "https://www.wrike.com/avatars/default/deleted.png",
    "timezone": "US/Pacific",
    "locale": "en",
    "deleted": True,
}

print(json["profiles"][0]["accountId"])
