import json
import pandas as pd
import requests
import openpyxl
from collections import defaultdict
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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



def check_min_at_mdg_010(data):
    with open('Min_value_validation_idp-sdi-mdg-000-010.txt', 'a') as f:
        for procuts_values in data['products'].values():
            for item_values in procuts_values['items'].values():
                    itemModifiersList = []
                    items_id = item_values.get('id')
                    item_name = item_values.get('name')
                    itemModifierGroups = item_values.get('itemModifierGroups')
                    if itemModifierGroups:
                        for values in itemModifierGroups:
                            prodGroupId = values.get('productGroupId')
                            min_itemGr = values.get('min')
                            itemModifiers = values.get('itemModifiers')
                            if prodGroupId == "idp-sdi-mdg-000-010":
                                for itemModifiers_keys, itemModifier_values in itemModifiers.items():
                                    if isinstance(itemModifier_values, dict) and 'itemModifiers' not in itemModifier_values:
                                        itemModifiersList.append(itemModifiers_keys)
                                if len(itemModifiersList) != min_itemGr:
                                    print(f'{items_id} -- discprepancy -- min value is {min_itemGr}, the number of single modifiers in {prodGroupId} is {len(itemModifiersList)} --- {item_name}')
                                    f.write(f'{items_id} -- discprepancy -- min value is {min_itemGr}, the number of single modifiers in {prodGroupId} is {len(itemModifiersList)} --- {item_name}\n')
                                else:
                                    print(f"{items_id} -- correct -- min value is {min_itemGr},  the number of single modifiers in {prodGroupId} is {len(itemModifiersList)} --- {item_name}")
                                    f.write(f"{items_id} -- correct -- min value is {min_itemGr},  the number of single modifiers in {prodGroupId} is {len(itemModifiersList)} --- {item_name}\n")





#api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/5575/channel/WEBOA/type/ALLDAY"
api_url11 = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/8810/channel/WEBOA/type/ALLDAY"
#api_url = f"https://menu-api-v0.snc-api.demo.irb.digital/menu/v1/brand/SDI/location/7996/channel/WEBOA/type/ALLDAY"

api = get_json_from_api(api_url11)
                        
check_min_at_mdg_010(api)