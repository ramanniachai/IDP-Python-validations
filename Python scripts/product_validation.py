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
            print(f"не удалось получить данные из API, код ответа {response.status_code}")
            data = None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса к API: {e}")
        data = None
        
    return data



available_locations = ['1122', '5575']




api_url = f"https://location-service-v2.api-idp.sonicdrivein.com/brand/SDI/location?size=10000"
api = get_json_from_api(api_url)

def get_all_locations(api):
    all_locations = []
    for info in api['content']:
        locationId = info.get('id')
        all_locations.append(locationId)

    return all_locations


#api = get_json_from_api(api_url)

all_locations = get_all_locations(api)
#print(all_locations)
#all_locationss = ['3581', '3588', '1760']
all_locationsss = ['5591', '5592', '5594', '5595', '5596', '5597', '5598', '5599', '5601', '5602', '5603', '5604', '5605', '5606', '5607', '5608', '5609', '5610', '5611', '5612', '5613', '5614', '5615', '5616', '5617', '5619', '5620', '5621', '5622', '5623', '5624', '5625', '5626', '5627', '5628', '5629', '5630', '5631', '5632', '5633', '5634', '5635', '5636', '5637', '5638', '5639', '5640', '5641', '5642', '5643', '5644', '5645', '5646', '5647', '5648', '5649', '5650', '5652', '5653', '5654', '5655', '5656', '5657', '5658', '5659', '5660', '5661', '5662', '5663', '5664', '5665', '5666', '5667', '5668', '5669', '5670', '5671', '5672', '5673', '5674', '5676', '5677', '5678', '5679', '5680', '5681', '5682', '5683', '5684', '5685', '5686', '5687', '5688', '5689', '5690', '5691', '5692', '5693', '5694', '5695', '5696', '5697', '5698', '5699', '5700', '5701', '5702', '5703', '5704', '5705', '5706', '5707', '5708', '5709', '5710', '5711', '5713', '5714', '5715', '5716', '5717', '5718', '5719', '5720', '5721', '5722', '5723', '5724', '5725', '5726', '5727', '5728', '5729', '5730', '5731', '5732', '5733', '5735', '5736', '5737', '5738', '5739', '5740', '5741', '5742', '5743', '5744', '5745', '5746', '5747', '5749', '5750', '5751', '5752', '5753', '5754', '5755', '5756', '5757', '5758', '5759', '5760', '5761', '5762', '5763', '5764', '5765', '5766', '5767', '5768', '5769', '5770', '5771', '5772', '5773', '5774', '5775', '5776', '5777', '5778', '5779', '5780', '5781', '5783', '5784', '5785', '5786', '5787', '5788', '5789', '5790', '5791', '5792', '5793', '5794', '5795', '5796', '5797', '5798', '5799', '5800', '5801', '5802', '5803', '5804', '5805', '5806', '5807', '5808', '5809', '5810', '5811', '5812', '5813', '5815', '5816', '5817', '5818', '5819', '5820', '5821', '5822', '5823', '5824', '5825', '5826', '5827', '5828', '5829', '5830', '5831', '5832', '5833', '5834', '5835', '5836', '5837', '5838', '5839', '5840', '5841', '5842', '5843', '5844', '5845', '5846', '5847', '5848', '5849', '5850', '5851', '5852', '5853', '5854', '5855', '5856', '5857', '5858', '5859', '5860', '5863', '5864', '5865', '5866', '5867', '5868', '5869', '5870', '5871', '5872', '5873', '5874', '5875', '5876', '5877', '5878', '5879', '5880', '5881', '5882', '5883', '5884', '5885', '5887', '5888', '5889', '5890', '5891', '5892', '5893', '5894', '5895', '5896', '5897', '5898', '5899', '5900', '5902', '5903', '5904', '5905', '5906', '5907', '5908', '5909', '5910', '5911', '5912', '5913', '5914', '5915', '5916', '5917', '5918', '5919', '5920', '5921', '5922', '5923', '5924', '5925', '5926', '5927', '5928', '5929', '5930', '5932', '5933', '5934', '5935', '5936', '5937', '5938', '5939', '5940', '5941', '5942', '5943', '5944', '5945', '5946', '5947', '5948', '5949', '5950', '5951', '5952', '5953', '5954', '5955', '5956', '5957', '5958', '5959', '5960', '5961', '5962', '5963', '5964', '5965', '5966', '5967', '5968', '5969', '5970', '5971', '5972', '5973', '5974', '5975', '5976', '5977', '5978', '5979', '5980', '5981', '5982', '5983', '5984', '5985', '5986', '5987', '5988', '5989', '5990', '5991', '5992', '5993', '5994', '5995', '5996', '5999', '6000', '6001', '6002', '6003', '6004', '6006', '6007', '6008', '6009', '6010', '6011', '6012', '6013', '6014', '6015', '6016', '6017', '6018', '6019', '6020', '6021', '6022', '6023', '6024', '6025', '6027', '6028', '6029', '6030', '6031', '6032', '6033', '6034', '6035', '6036', '6037', '6038', '6039', '6040', '6042', '6043', '6044', '6045', '6046', '6047', '6048', '6049', '6050', '6051', '6052', '6053', '6054', '6055', '6056', '6057', '6059', '6060', '6061', '6062', '6063', '6064', '6065', '6066', '6068', '6069', '6070', '6071', '6072', '6073', '6074', '6075', '6076', '6077', '6078', '6079', '6080', '6081', '6082', '6083', '6084', '6085', '6086', '6087', '6088', '6089', '6090', '6091', '6093', '6094', '6095', '6096', '6097', '6098', '6099', '6100', '6101', '6102', '6103', '6104', '6105', '6106', '6107', '6108', '6109', '6111', '6112', '6113', '6114', '6115', '6116', '6117', '6118', '6119', '6120', '6121', '6122', '6123', '6124', '6125', '6126', '6127', '6128', '6129', '6130', '6131', '6132', '6133', '6134', '6135', '6136', '6137', '6138', '6139', '6140', '6141', '6142', '6143', '6144', '6145', '6146', '6147', '6148', '6149', '6151', '6152', '6153', '6154', '6155', '6156', '6157', '6158', '6159', '6160', '6161', '6162', '6163', '6164', '6165', '6166', '6167', '6168', '6169', '6170', '6171', '6172', '6173', '6174', '6175', '6176', '6177', '6178', '6179', '6180', '6181', '6182', '6183', '6184', '6185', '6186', '6187', '6188', '6189', '6191', '6192', '6193', '6194', '6195', '6196', '6197', '6198', '6199', '6200', '6201', '6202', '6203', '6204', '6205', '6206', '6207', '6208', '6209', '6210', '6211', '6212', '6213', '6214', '6216', '6217', '6218', '6219', '6220', '6221', '6222', '6223', '6224', '6225', '6226', '6227', '6228', '6229', '6230', '6231', '6232', '6233', '6234', '6235', '6236', '6237', '6238', '6239', '6240', '6241', '6242', '6243', '6244', '6245', '6246', '6247', '6248', '6249', '6250', '6251', '6252', '6253', '6254', '6255', '6256', '6257', '6258', '6259', '6260', '6261', '6262', '6263', '6264', '6265', '6267', '6268', '6269', '6270', '6271', '6272', '6273', '6274', '6275', '6276', '6277', '6278', '6279', '6280', '6281', '6282', '6283', '6284', '6285', '6286', '6287', '6288', '6289', '6290', '6291', '6292', '6293', '6294', '6295', '6296', '6297', '6298', '6299', '6300', '6301', '6303', '6304', '6305', '6306', '6307', '6308', '6309', '6310', '6311', '6312', '6313', '6314', '6315', '6317', '6318', '6319', '6320', '6321', '6323', '6324', '6325', '6326', '6327', '6328', '6329', '6330', '6334', '6335', '6336', '6337', '6338', '6339', '6340', '6341', '6342', '6343', '6344', '6345', '6346', '6347', '6349', '6350', '6351', '6352', '6353', '6354', '6355', '6358', '6359', '6360', '6361', '6362', '6363', '6364', '6365', '6366', '6367', '6368', '6369', '6370', '6371', '6373', '6374', '6375', '6376', '6377', '6378', '6379', '6380', '6381', '6382', '6383', '6384', '6385', '6386', '6387', '6388', '6389', '6390', '6391', '6392', '6393', '6394', '6395', '6396', '6397', '6398', '6399', '6400', '6401', '6402', '6403', '6405', '6406', '6408', '6409', '6410', '6411', '6412', '6413', '6414', '6415', '6416', '6417', '6418', '6419', '6420', '6421', '6422', '6423', '6424', '6425', '6426', '6427', '6428', '6429', '6430', '6431', '6432', '6433', '6434', '6435', '6436', '6437', '6438', '6439', '6440', '6441', '6442', '6443', '6444', '6445', '6446', '6447', '6448', '6449', '6450', '6451', '6453', '6454', '6455', '6456', '6457', '6458', '6459', '6460', '6461', '6462', '6463', '6464', '6465', '6466', '6467', '6468', '6469', '6470', '6471', '6472', '6473', '6474', '6475', '6476', '6477', '6478', '6479', '6480', '6481', '6482', '6483', '6484', '6485', '6486', '6487', '6488', '6489', '6490', '6491', '6493', '6494', '6495', '6496', '6497', '6498', '6499', '6500', '6501', '6502', '6503', '6505', '6506', '6507', '6508', '6509', '6510', '6511', '6512', '6513', '6514', '6515', '6516', '6518', '6519', '6520', '6521', '6522', '6523', '6524', '6525', '6526', '6527', '6528', '6529', '6530', '6531', '6532', '6533', '6534', '6535', '6536', '6537', '6538', '6539', '6540', '6541', '6542', '6543', '6544', '6545', '6546', '6547', '6548', '6549', '6550', '6551', '6552', '6553', '6554', '6555', '6556', '6557', '6558', '6559', '6560', '6561', '6562', '6563', '6564', '6565', '6566', '6567', '6568', '6569', '6570', '6571', '6572', '6573', '6574', '6575', '6576', '6577', '6578', '6579', '6580', '6581', '6582', '6583', '6584', '6585', '6586', '6587', '6588', '6589', '6590', '6591', '6592', '6593', '6594', '6595', '6596', '6597', '6598', '6599', '6600', '6601', '6602', '6603', '6604', '6605', '6606', '6607', '6608', '6609', '6610', '6611', '6612', '6613', '6614', '6615', '6616', '6617', '6618', '6619', '6620', '6621', '6622', '6623', '6624', '6625', '6626', '6627', '6628', '6629', '6630', '6631', '6632', '6633', '6634', '6635', '6636', '6637', '6638', '6639', '6640', '6641', '6642', '6643', '6644', '6645', '6646', '6647', '6648', '6649', '6650', '6651', '6652', '6653', '6654', '6655', '6656', '6657', '6658', '6659', '6660', '6661', '6662', '6663', '6664', '6665', '6666', '6667', '6668', '6669', '6670', '6671', '6672', '6673', '6674', '6675', '6676', '6677', '6678', '6679', '6680', '6681', '6682', '6683', '6684', '6685', '6686', '6687', '6688', '6689', '6690', '6691', '6692', '6693', '6694', '6695', '6696', '6697', '6698', '6699', '6700', '6701', '6702', '6703', '6704', '6705', '6706', '6707', '6708', '6709', '6710', '6711', '6712', '6713', '6714', '6715', '6716', '6717', '6718', '6719', '6720', '6721', '6722', '6723', '6724', '6725', '6726', '6727', '6728', '6729', '6730', '6731', '6732', '6733', '6734', '6735', '6736', '6737', '6738', '6739', '6740', '6741', '6742', '6743', '6744', '6745', '6746', '6747', '6748', '6749', '6750', '6751', '6752', '6753', '6754', '6755', '6756', '6760', '6762', '6763', '6764', '6768', '6769', '6771', '6772', '6774', '6777', '6778', '6779', '6780', '6781', '6782', '6783', '6784', '6785', '6786', '6787', '6788', '6789', '6790', '6791', '6792', '6793', '6794', '6795', '6796', '6797', '6798', '6799', '6800', '6801', '6802', '6804', '6805', '6806', '6807', '6808', '6809', '6810', '6811', '6812', '6813', '6814', '6815', '6816', '6817', '6818', '6819', '6820', '6821', '6822', '6823', '6824', '6825', '6826', '6827', '6828', '6829', '6830', '6831', '6832', '6833', '6834', '6835', '6836', '6837', '6838', '6839', '6840', '6841', '6842', '6843', '6844', '6845', '6846', '6847', '6848', '6849', '6850', '6851', '6852', '6853', '6854', '6855', '6856', '6857', '6859', '6860', '6861', '6862', '6863', '6864', '6865', '6866', '6868', '6869', '6870', '6871', '6872', '6873', '6874', '6875', '6876', '6878', '6879', '6880', '6881', '6882', '6883', '6884', '6885', '6886', '6887', '6888', '6889', '6890', '6891', '6892', '6893', '6894', '6895', '6897', '6898', '6899', '6900', '6901', '6902', '6903', '6904', '6905', '6906', '6908', '6909', '6910', '6911', '6912', '6913', '6914', '6915', '6917', '6918', '6919', '6920', '6921', '6922', '6923', '6924', '6925', '6926', '6928', '6929', '6930', '6931', '6932', '6933', '6935', '6936', '6937', '6938', '6939', '6940', '6941', '6942', '6945', '6946', '6947', '6948', '6949', '6950', '6951', '6952', '6953', '6954', '6955', '6957', '6958', '6959', '6960', '6961', '6962', '6963', '6964', '6965', '6966', '6967', '6969', '6971', '6972', '6973', '6974', '6975', '6976', '6977', '6979', '6980', '6981', '6982', '6983', '6984', '6985', '6986', '6987', '6988', '6989', '6990', '6991', '6993', '6994', '6995', '6996', '6997', '6998', '6999', '7000', '7001', '7002', '7003', '7004', '7005', '7006', '7007', '7009', '7010', '7014', '7015', '7016', '7017', '7018', '7019', '7020', '7021', '7023', '7024', '7025', '7026', '7027', '7028', '7029', '7030', '7031', '7032', '7033', '7034', '7035', '7037', '7038', '9007', '9600']
corpus = ['1182', '1735', '1776', '2292', '2832', '3711', '3854', '3868', '4025', '4118', '4511', '4609', '4659', '5030', '5106', '5613', '5707', '6657', '6923', '6912']
tri = ['1091', '1697', '1996', '2282', '2290', '2320', '3480', '3664', '3700', '4156', '4323', '5763', '5839']
milwauke = ['6086']
portland = ['5608', '5878', '5887', '5888', '6119', '6206', '6335']
seatle = ['5932', '5990', '6109', '6185', '6221', '6456', '6514', '6540', '6544', '6619', '6635', '6652', '6660', '6813', '6983']
harlingen = ['2139', '2205', '3887', '3931', '4149', '4179', '4244', '4831', '6777', '6930', '6900', '6769', '6800', '6809']
jackson = ['1558', '2172', '2198', '2251', '2273', '2284', '2351', '2484', '2753', '2890', '3015', '4348', '5222', '5946']
knoxville = ['1267', '1807', '2166', '2219', '2266', '2315', '2319', '2360', '2403', '2490', '2513', '2573', '2678', '2945', '3134', '3183', '3327', '3333', '3487', '3489', '3591', '3771', '3820', '3824', '3900', '4437', '4789', '5154', '5325', '5502', '5650', '5727', '5753', '5789', '6029', '6053', '6393', '6789', '6790']
nashville = ['1193', '1318', '1588', '1816', '1833', '1836', '1850', '1874', '1917', '1925', '2012', '2019', '2064', '2124', '2136', '2164', '2197', '2222', '2226', '2338', '2400', '2416', '2421', '2473', '2538', '2541', '2563', '2564', '2585', '2624', '2625', '2627', '2630', '2631', '2655', '2712', '2716', '2746', '2809', '2893', '2946', '2957', '2969', '2984', '2996', '3033', '3102', '3104', '3275', '3323', '3357', '3372', '3417', '3453', '3468', '3488', '3503', '3504', '3548', '3554', '3576', '3604', '3649', '3679', '3704', '3749', '3752', '3790', '3835', '3836', '3839', '3977', '4045', '4053', '4110', '4165', '4173', '4193', '4224', '4234', '4446', '4481', '4515', '4732', '4750', '4755', '4770', '4972', '5061', '5115', '5149', '5289', '5321', '5330', '5331', '5454', '5499', '5580', '5662', '5715', '5737', '5766', '5791', '5909', '6028', '6397', '6436', '6461', '6613', '6625', '6640', '6942']
sanant = ['1756', '1839', '1931', '1956', '2059', '2104', '2200', '2310', '2594', '2735', '2740', '2853', '2869', '2873', '2904', '2912', '2943', '2949', '2950', '2952', '2955', '2959', '2970', '2971', '2973', '2976', '2981', '2983', '3058', '3376', '3381', '3465', '3515', '3532', '3630', '3659', '3696', '3709', '3751', '3841', '3849', '3851', '3898', '3933', '3934', '4043', '4060', '4094', '4117', '4135', '4136', '4185', '4276', '4421', '4451', '4575', '4869', '4896', '5110', '5134', '5158', '5210', '5214', '5227', '5233', '5251', '5292', '5333', '5391', '5439', '5676', '5703', '5811', '5918', '6211', '6413', '6450', '6475', '6476', '6562', '6601', '6615', '6623', '6656', '6688', '6707', '6741', '6748', '6763', '6772', '6998']

'''
def price_at_all_corpus(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-82290-8890-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                        #else:
                         #   current_price = item_price.get('currentPrice')
                          #  if current_price == 0 or current_price == 0.00:
                           #     print(f"8/13/2024 | {location} | {items_name} | {current_price}")
                            #    result = f"8/13/2024 | {location} | {items_name} | {current_price}\n"
                             #   f.write(result)



data_list = []
for location in corpus:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_corpus(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def price_at_all_tri(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-82290-8890-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                        #else:
                         #   current_price = item_price.get('currentPrice')
                          #  if current_price == 0 or current_price == 0.00:
                           #     print(f"8/13/2024 | {location} | {items_name} | {current_price}")
                            #    result = f"8/13/2024 | {location} | {items_name} | {current_price}\n"
                             #   f.write(result)



data_list = []
for location in tri:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_tri(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)




def price_at_all_milwauke(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-40342-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-40340-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-40343-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42670-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42680-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)


data_list = []
for location in milwauke:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_milwauke(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def price_at_all_portland(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-18650-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-18660-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-18670-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in portland:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_portland(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def price_at_all_seatle(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-26890-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in seatle:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_seatle(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def price_at_all_harling(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-27540-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in harlingen:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_harling(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)


def price_at_all_jackson(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-41530-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-32750-41530":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-41590-000":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-32750-41590":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in jackson:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = price_at_all_jackson(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def items_at_knoxville(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-26890-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in knoxville:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = items_at_knoxville(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def items_at_nashville(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-26890-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42670-000":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42680-000":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in nashville:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = items_at_nashville(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)



def items_at_sanantonio(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Raw Prices 12062024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-27540-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42670-000":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-42680-000":
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)



data_list = []
for location in sanant:
    result = {}
    api_url = f"https://api-idp.sonicdrivein.com/snc/menu-api/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url = f"https://menu-api-v0.snc-api.uat.irb.digital/menu/v1/brand/SDI/location/{location}/channel/WEBOA/type/ALLDAY"
    #api_url1 = f"https://api-idp.sonicdrivein.com/snc/web-exp-api/v1/menu/type/ALLDAY/id/{location}?sellingChannel=WEBOA"
    api_data = get_json_from_api(api_url)
    if api_data is not None:
        result = items_at_sanantonio(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)
'''


def items_at_newdrinks(api, location):
    size_id_to_name = {}
    for size_values in api['sizeGroups'].values():
        size_id_to_name[size_values['id']] = size_values['name'] 

    with open('Drinks_Raw Prices 12162024.txt', 'a') as f:
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
                if item_id == "idp-sdi-itm-82640-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
                        print(f"{current_utc_time} | {location} | {items_name} | No price")
                        result = f"{current_utc_time} | {location} | {items_name} | No price\n"
                        f.write(result)

                if item_id == "idp-sdi-itm-82650-000":
                    
                    #if item_group != 'idp-sdi-itg-999-999':
                            #all_items_at_this_location.append(item_keys)
                        #print(all_items_at_this_location)
                        #for i in all_items_at_this_location:
                            #if item_keys == i:
                    item_price = item_values.get('price')

                    if item_price:
                                #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = item_price.get('currentPrice')
                        print(f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}")
                        result = f"{current_utc_time} | {location} | {items_name} | {item_price.get('currentPrice')}\n"
                        f.write(result)
                    if item_price == {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = 'empty {}'
                        print(f"{current_utc_time} | {location} | {items_name} | Empty {{}}")
                        result = f"{current_utc_time} | {location} | {items_name} | Empty{{}}\n"
                        f.write(result)
                    elif not item_price and item_price != {}:
                                                    #data[f"{items_dict[i]} {size_id_to_name[item_size]}"]  = None
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
        result = items_at_newdrinks(api_data, location)
    else:
        result = {'location': location, 'price': 'Failed to get data for location'}
    data_list.append(result)
