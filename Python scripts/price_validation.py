import json
import pandas as pd
import requests
import openpyxl
from collections import defaultdict
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from datetime import datetime




def get_json_from_api(url):
    try:
        #response = requests.get(url)
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
        else:
            print(f"Unable to retrieve data from API, status cide is {response.status_code}")
            data = None
    except requests.exceptions.RequestException as e:
        print(f"Error while sending API request: {e}")
        data = None
        
    return data




def get_all_locations(api):
    all_locations = []
    for info in api['content']:
        locationId = info.get('id')
        all_locations.append(locationId)

    return all_locations

api_url = f"https://location-service-v2.api-idp.sonicdrivein.com/brand/SDI/location?size=10000"
api = get_json_from_api(api_url)


all_locations = get_all_locations(api)
#all_locationss = []


def price_in_newProducts(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 01062025.txt', 'a') as f:
        all_items_at_this_location = []
        last_updated_timestamp = api.get('lastUpdatedTimestamp')
        current_utc_time = datetime.utcnow()
        for values in api['products'].values():
            product_type = values.get('type')
            for item_keys, item_values in values['items'].items():
                items_name = item_values["name"]   
                item_id = item_values["id"]
                item_size = item_values.get('sizeGroupId')
                item_group = item_values.get('itemGroupId')
                if item_id == "idp-sdi-itm-81730-000":
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

                if item_id == "idp-sdi-itm-82770-81730-000":
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
                    
                if item_id == "idp-sdi-itm-81750-000":
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

                if item_id == "idp-sdi-itm-82780-81750-000":
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

                if item_id == "idp-sdi-itm-82800-000":
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

                if item_id == "idp-sdi-itm-82803-000":
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

                if item_id == "idp-sdi-itm-82804-000":
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

                if item_id == "idp-sdi-itm-82121-000":
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

                if item_id == "idp-sdi-itm-82122-000":
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

                if item_id == "idp-sdi-itm-82120-000":
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

                if item_id == "idp-sdi-itm-82123-000":
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

                if item_id == "idp-sdi-itm-82124-000":
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


data_list = []
for location in all_locations:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_in_newProducts(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)
