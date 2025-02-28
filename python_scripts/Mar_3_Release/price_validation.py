import json
import pandas as pd
import requests
from datetime import datetime
from findLocations import get_all_location_ids_sanity, get_all_location_ids


def get_json_from_api(url):
    try:
        #response = requests.get(url)
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
        else:
            print(f"Unable to retrieve data from API, status code is {response.status_code}")
            data = None
    except requests.exceptions.RequestException as e:
        print(f"Error while sending API request: {e}")
        data = None
        
    return data


all_local_locations_sanity = get_all_location_ids_sanity()
all_local_locations = get_all_location_ids()
#all_locationss = []

item_ids_input = input("Specify item ID/IDs that you wanna check, separated by spaces: ")
item_to_check = item_ids_input.split()

def price_in_newProducts(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 03032025.txt', 'a') as f:
        last_updated_timestamp = api.get('lastUpdatedTimestamp')
        current_utc_time = datetime.utcnow()
        for values in api['products'].values():
            product_type = values.get('type')
            for item_keys, item_values in values['items'].items():
                items_name = item_values["name"]   
                item_id = item_values["id"]
                item_size = item_values.get('sizeGroupId')
                item_group = item_values.get('itemGroupId')

                for i in item_to_check:
                    if item_id == i and item_size == "idp-sdi-sig-999-999":
                        item_price = item_values.get('price')

                        if item_price:
                            print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                            result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                            f.write(result)
                        if item_price == {}:
                            print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                            result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                            f.write(result)
                        elif not item_price and item_price != {}:
                            print(f"{current_utc_time} | {location} | {items_name} | No price")
                            result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                            f.write(result)

                    if item_id == i and item_size != "idp-sdi-sig-999-999":
                        item_price = item_values.get('price')

                        if item_price:
                            print(f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | {item_price.get('currentPrice')}")
                            result = f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | {item_price.get('currentPrice')}\n"
                            f.write(result)
                        if item_price == {}:
                            print(f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | Empty {{}}")
                            result = f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | Empty{{}}\n"
                            f.write(result)
                        elif not item_price and item_price != {}:
                            print(f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | No price")
                            result = f"{current_utc_time} | {location} | {items_name} {size_id_to_name[item_size]} | No price\n"
                            f.write(result)


data_list = []
for location in all_local_locations_sanity:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_in_newProducts(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)