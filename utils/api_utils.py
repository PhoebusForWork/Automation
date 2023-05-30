# -*- coding: utf-8 -*-
import requests
import json
import inspect
import datetime
from utils.data_utils import EnvReader
from utils.generate_utils import Make

env = EnvReader()
platform_host = env.PLATFORM_HOST
platform_header = env.PLT_HEADER
cs_host = env.WEB_HOST
control_host = env.CONTROL_HOST
cs_header = env.CS_HEADER
xxl_host = env.XXL_HOST


class API_Controller:

    def __init__(self, platform='plt'):

        self.current_timestamp = str(int(datetime.datetime.now().timestamp()))
        self.request_session = requests.Session()
        self.platform = platform
        if self.platform == 'plt':
            self.host = platform_host
            # 這邊字串轉為dict要使用eval不可用dict會掛
            self.request_session.headers = eval(platform_header)
        elif self.platform == 'xxl':
            self.host = xxl_host
        elif self.platform == 'control':
            self.host = control_host
        else:
            self.host = cs_host
            self.request_session.headers = eval(cs_header)

    @staticmethod
    def print_response(response):  # 印出回傳
        print('\n\n--------------HTTPS response  *  begin ------------------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k};{v}')

        print('')
        response_text = json.loads(response.text)
        print(
            json.dumps(response_text,
                       sort_keys=True,
                       indent=4,
                       separators=(',', ': '),
                       ensure_ascii=False))
        print('--------------HTTPS response  *  end ------------------\n\n')

    def __update_sign(self):
        device_id = self.request_session.headers.get("device-id", "")
        os_type = self.request_session.headers.get("os-type", "")
        if self.platform == 'plt':
            secret = env.PLT_SECRET
        else:
            secret = env.CS_SECRET
        sign = Make.sign(device_id=device_id, SECRET=secret, os_type=os_type)
        self.request_session.headers.update(sign)

    def send_request(self, method, url, json=None, params=None, token=None, files=None):
        if token:
            self.request_session.headers.update({"token": str(token)})
        self.__update_sign()
        request_body = {
            "url": self.host + url,
            "json": json,
            "params": params,
            "files": files
        }

        if method == 'post':
            response = self.request_session.post(**request_body)
        elif method == 'put':
            response = self.request_session.put(**request_body)
        elif method == 'get':
            response = self.request_session.get(**request_body)
        elif method == 'delete':
            response = self.request_session.delete(**request_body)
        else:
            response = "沒有符合的請求模式"
        try:
            self.print_response(response)
        except Exception:
            pass
        return response


class KeywordArgument:

    @staticmethod
    def body_data(filter: list = None):
        if filter is None:
            filter = ['self', 'plat_token']
        caller = inspect.stack()[1][0]
        args, _, _, values = inspect.getargvalues(caller)
        r = dict()
        for i in args:
            if i not in filter and values[i] is not None:
                r[i] = values[i]
        return r


if __name__ == "__main__":
    pass
