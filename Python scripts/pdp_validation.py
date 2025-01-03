import json
import pandas as pd
import requests
import openpyxl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from collections import OrderedDict



def get_json_from_api(url):
    try:
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
        else:
            print(f"Unable to retrieve data from API, status cide is {response.status_code}")
            data = None
    except requests.exceptions.RequestException as e:
        print(f"Error while sending API requiest: {e}")
        data = None
        
    return data



def retrieve_the_whole_structure_of_items_excel1(api, category, new_products):
    modifierGroup_dict = {}
    items_dict = {}
    intensityGroup_dict = {}
    category_id_to_name = {}
    size_id_to_name = {}


    for productGroup_values in api['productGroups'].values():
        modifierGroup_dict[productGroup_values['id']] = productGroup_values['name']

    for products_values in api['products'].values():
        for item_keys, item_values in products_values['items'].items():
            items_dict[item_values['id']] = item_values['name']

    for itemGroup_values in api['itemGroups'].values():
        intensityGroup_dict[itemGroup_values['id']] = itemGroup_values['name']

    for category_values in api['categories'].values():
        category_id_to_name[category_values['id']] = category_values['name']

    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name']    


    size_order = ["Mini", "Sm", "Med", "Reg", "Lg", "RT 44®", 'Sm (4pc)', 'Med (6pc)', 'Lg (8pc)', 'Sm (3pc)', 'Med (5pc)', 'Lg (7pc)', '20pc', 'NONE', 'NO', 'ADD', 'EASY', 'EXTRA'] 

    for product_values in api['products'].values():
        items = list(product_values['items'].values())
        sorted_items = sorted(items, key=lambda item: size_order.index(size_id_to_name.get(item.get("sizeGroupId", ""), "NONE")))
        product_values['items'] = {item['id']: item for item in sorted_items}



    headers = ['Category', 'ItemName', 'ModifierGroup'] + [str(i+1) for i in range(67)]
    data = [headers]
    current_category = None

    sorted_products = sorted(api['products'].values(), key=lambda k: k['name'])

    for i in category:  

        for product_values in sorted_products:
            for items_keys, items_values in product_values['items'].items():

                item_category = items_values.get('categoryIds')
                if item_category is None or i not in item_category:
                    continue

                item_name = items_values.get('name')
                item_id = items_values.get('id')
                item_size = items_values.get('sizeGroupId')
                itemModifierGroups = items_values.get('itemModifierGroups')

                if item_name in new_products:
                    continue

                if not itemModifierGroups:
                    if item_size != 'idp-sdi-sig-999-999':
                        item_with_size = f"{item_name} {size_id_to_name[item_size]}: "
                    else:
                        item_with_size = f"{item_name}: "

                    row = [None]*70
                    if i != current_category:
                        current_category = i
                        row[0] = category_id_to_name[i]
                    row[1] = item_with_size
                    data.append(row)
                    continue


                if itemModifierGroups:
                    if item_size != 'idp-sdi-sig-999-999':
                        item_with_size = f"{item_name} {size_id_to_name[item_size]}: "
                    else:
                        item_with_size = f"{item_name}: "

                    sorted_itemModifierGroups = sorted(itemModifierGroups, key=lambda x: x.get('sequence', 0))


                    for itemModifierGroups_list_values in sorted_itemModifierGroups:
                        row = [None]*70
                        modifierGroup = itemModifierGroups_list_values.get('productGroupId')
                        itemModifiers = itemModifierGroups_list_values.get('itemModifiers')

                        if i != current_category:
                            current_category = i
                            row[0] = category_id_to_name[i]
                        row[1] = item_with_size
                        columnIndex = 2


                        if modifierGroup:
                            row[columnIndex] = modifierGroup_dict.get(modifierGroup)
                            columnIndex += 1
                        sorted_itemModifiers = sorted(list(itemModifiers.values()), key=lambda x: x.get('sequence', 0))
                        

                        for itemModifiers_values in sorted_itemModifiers:

                            single_mod_and_intensityGr_sequence = itemModifiers_values.get('sequence')
                            itemModifier2 = itemModifiers_values.get('itemModifiers')


                            if not itemModifier2:
                                singleModifierId = itemModifiers_values.get('itemId')
                                row[columnIndex] = items_dict.get(singleModifierId)
                                columnIndex += 1
                             
                            if itemModifier2:    
                                intensity_modifiers = []
                                for itemModifier2_list_values in sorted(itemModifier2, key=lambda x: x.get('sequence', 0)):
                                    if items_dict.get(itemModifier2_list_values.get('itemId'), '') not in new_products:
                                        intensity_modifiers.append(items_dict.get(itemModifier2_list_values.get('itemId'), ''))
                                
                                

                                intensity_modifiers_str = '\n'.join(intensity_modifiers)
                                if intensity_modifiers_str:  
                                    row[columnIndex] = intensity_modifiers_str
                                    columnIndex += 1
                        data.append(row)

    df = pd.DataFrame(data[1:], columns=data[0])

    writer = pd.ExcelWriter('Regresison_UAT2.xlsx', engine='xlsxwriter')

    df.to_excel(writer, index=False, sheet_name="Report")

    workbook = writer.book
    worksheet = writer.sheets['Report']

    wrap_format = workbook.add_format({'text_wrap': True})

    for i, col in enumerate(df.columns):
        # find length of column i
        column_len = df[col].astype(str).str.len().max()
        #print(column_len)
        # Setting the length if the column header is larger
        # than the max column value length
        column_len = max(column_len, len(str(col))) + 2
        # set the column length
        worksheet.set_column(i, i, column_len, wrap_format)

    writer._save()

new_products = ['Bacon Deluxe Double SONIC® Smasher', 'Bacon Deluxe Double SONIC® Smasher Combo', 'Bacon Deluxe Triple SONIC® Smasher', 'Bacon Deluxe Triple SONIC® Smasher Combo', 'Sour Dragon Fruit Recharger with Red Bull®', 'Strawberry Fusion Fizz', 'Grape Escape', 'Buttery Brew', 'The Pairs', 'The Nicole', 'Double SONIC Queso Smasher', 'Triple SONIC Queso Smasher', 'Red Velvet Cake Batter Shake', '$4.99 Feast']
category = ['idp-sdi-cat-000-067', 'idp-sdi-cat-000-013', 'idp-sdi-cat-000-014', 'idp-sdi-cat-000-015', 'idp-sdi-cat-000-016', 'idp-sdi-cat-000-017', 'idp-sdi-cat-000-018', 'idp-sdi-cat-000-019', 'idp-sdi-cat-000-021', 'idp-sdi-cat-000-022', 'idp-sdi-cat-000-038', 'idp-sdi-cat-000-039', 'idp-sdi-cat-000-049', 'idp-sdi-cat-000-052', 'idp-sdi-cat-000-051', 'idp-sdi-cat-000-053', 'idp-sdi-cat-000-027', 'idp-sdi-cat-000-028' , 'idp-sdi-cat-000-024', 'idp-sdi-cat-000-025', 'idp-sdi-cat-000-034', 'idp-sdi-cat-000-035', 'idp-sdi-cat-000-036', 'idp-sdi-cat-000-032', 'idp-sdi-cat-000-030', 'idp-sdi-cat-000-031', 'idp-sdi-cat-000-010', 'idp-sdi-cat-000-009', 'idp-sdi-cat-000-075', 'idp-sdi-cat-000-077', 'idp-sdi-cat-000-095', 'idp-sdi-cat-000-089', 'idp-sdi-cat-000-090', 'idp-sdi-cat-000-091', 'idp-sdi-cat-000-092', 'idp-sdi-cat-000-096', 'idp-sdi-cat-000-097', 'idp-sdi-cat-000-098', 'idp-sdi-cat-000-003', 'idp-sdi-cat-000-068']



#api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/6273/channel/WEBOA/type/ALLDAY"
api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/8810/channel/WEBOA/type/ALLDAY"
#api_url = f"https://menu-api-v0.snc-api.demo.irb.digital/menu/v1/brand/SDI/location/7996/channel/WEBOA/type/ALLDAY"
api = get_json_from_api(api_url)

retrieve_the_whole_structure_of_items_excel1(api, category, new_products)


