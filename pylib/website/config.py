# -*- coding: utf-8 -*-
import configparser
from ..website.webApiBase import WEB_API  # 執行RF時使用
from utils.generate_utils import Make


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']


class Config(WEB_API):  # 客戶詳細資料

    def get_avatar_urls(self):  # 獲取用戶明細資料
        response = self.ws.get(web_host+"/v1/config/avatar/urls",
                               data={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()
