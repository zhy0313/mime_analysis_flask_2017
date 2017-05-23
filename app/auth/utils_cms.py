import datetime
import random
import requests


api_host = r'http://sms-api.luosimao.com/v1/send.json'
api_key = r'key-4efc7922b1bc90b949a2fa073519eb61'


def generate_code():
    code_list = [str(random.randrange(0, 9)) for i in range(4)]
    ret_code = ''.join(code_list)
    return ret_code


def send_sms_code(phone, code):
    global api_host
    global api_key

    cmd_str = api_host
    auth_tuple = ("api", api_key)

    data_dict = dict()
    data_dict['mobile'] = phone
    data_dict['message'] = '{key}【迈德科技】'.format(key=code)

    response = requests.post(cmd_str, auth=auth_tuple, data=data_dict, timeout=3, verify=False)
    if response.json()['error'] != 0:
        return False
    return True
