import os
from program.utils.hubspot_api import hubspot_request
from program.utils.hubspot_api_exection import HubspotAPIError


def format_properties_url(properties: list[str]) -> str:
    return "&properties={}".format("&properties=".join(properties))


def get_all_product_properties():
    url = "https://api.hubapi.com/crm/v3/properties/products"
    response = hubspot_request(os.getenv("PRIVATE_APP_KEY"), url, "GET")
    properties = []
    for property in response.data["results"]:
        properties.append(property["name"])
    return properties


def get_all_products(properties: list[str]):
    url = f"https://api.hubapi.com/crm/v3/objects/products?archived=false&limit=100" + format_properties_url(properties)
    response = hubspot_request(os.getenv("PRIVATE_APP_KEY"), url, "GET").get_all_results()
    return response
