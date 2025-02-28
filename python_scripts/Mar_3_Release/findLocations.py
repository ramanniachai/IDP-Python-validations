import json
import pandas as pd
import requests
import openpyxl
from collections import defaultdict

file_path = 'Markets.xlsx'
df = pd.read_excel(file_path)

def get_location_ids_sanity(market_id):
    url = 'https://location-service-v2.api-idp.sonicdrivein.com/brand/SDI/category/INCLUSION/group?page=0&size=10000'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for market in data['content']:
            if market['id'] == market_id:
                location_ids = [location['id'] for location in market['locations'][:2]]
                return location_ids
    return []

def get_all_location_ids_sanity():
    all_location_ids_sanity = []
    for market_id in df['IDs']:
        location_ids = get_location_ids_sanity(market_id)
        all_location_ids_sanity.extend(location_ids)
    return all_location_ids_sanity

def get_location_ids(market_id):
    url = 'https://location-service-v2.api-idp.sonicdrivein.com/brand/SDI/category/INCLUSION/group?page=0&size=10000'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for market in data['content']:
            if market['id'] == market_id:
                location_ids = [location['id'] for location in market['locations']]
                return location_ids
    return []


def get_all_location_ids():
    all_location_ids = []
    for market_id in df['IDs']:
        location_ids = get_location_ids(market_id)
        all_location_ids.extend(location_ids)
    return all_location_ids