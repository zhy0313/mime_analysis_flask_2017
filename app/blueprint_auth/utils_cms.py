import random
import requests
from ..config import SMS_API_HOST
from ..config import SMS_API_KEY


def generate_code():
    code_list = [str(random.randrange(0, 9)) for i in range(4)]
    ret_code = ''.join(code_list)
    return ret_code


def send_sms_code(phone, code):
    cmd_str = SMS_API_HOST
    auth_tuple = ("api", SMS_API_KEY)

    data_dict = dict()
    data_dict['mobile'] = phone
    data_dict['message'] = '{key}【迈德科技】'.format(key=code)

    response = requests.post(cmd_str, auth=auth_tuple, data=data_dict, timeout=3, verify=False)
    if response.json()['error'] != 0:
        return False
    return True
