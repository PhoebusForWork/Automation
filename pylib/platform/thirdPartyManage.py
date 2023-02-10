# -*- coding: utf-8 -*-
from ..platform.platApiBase import PLAT_API
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


class thirdPartyManage(PLAT_API):

    def getThirdInterface(self,  # 獲取三方接口列表
                          plat_token=None,
                          type=None,
                          ):
        if plat_token != None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/thirdPartyManage",
                               json={},
                               params={
                                   "type": type,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def editThirdInterface(self,  # 編輯三方接口列表
                           plat_token=None,
                           id=None, name=None, template=None,
                           weighting=None, isEnabled=None,
                           ):
        if plat_token != None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/thirdPartyManage",
                               json=[{
                                   "id": id,
                                   "name": name,
                                   "template": template,
                                   "weighting": weighting,
                                   "isEnabled": isEnabled,
                               }],
                               params={}
                               )
        self._printresponse(response)
        return response.json()
