import random
import requests


def generate_code():
    code_list = [str(random.randrange(0, 9)) for i in range(4)]
    ret_code = ''.join(code_list)
    return ret_code


def send_sms_code(host, key, phone, code):
    cmd_str = host
    auth_tuple = ("api", key)

    data_dict = dict()
    data_dict['mobile'] = phone
    data_dict['message'] = '{key}【迈德科技】'.format(key=code)

    response = requests.post(cmd_str, auth=auth_tuple, data=data_dict, timeout=3, verify=False)
    if response.json()['error'] != 0:
        return False
    return True
