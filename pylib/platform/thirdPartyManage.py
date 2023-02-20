# -*- coding: utf-8 -*-
from ..platform.platApiBase import PlatformAPI
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


class ThirdPartyManage(PlatformAPI):

    def getThirdInterface(self,  # 獲取三方接口列表
                          plat_token=None,
                          type=None,
                          ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/thirdPartyManage",
                               json={},
                               params={
                                   "type": type,
                               }
                               )
        self.print_response(response)
        return response.json()

    def editThirdInterface(self,  # 編輯三方接口列表
                           plat_token=None,
                           id=None, name=None, template=None,
                           weighting=None, isEnabled=None,
                           ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/thirdPartyManage",
                               json=[{
                                   "id": id,
                                   "name": name,
                                   "template": template,
                                   "weighting": weighting,
                                   "isEnabled": isEnabled,
                               }],
                               params={}
                               )
        self.print_response(response)
        return response.json()
