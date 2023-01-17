# -*- coding: utf-8 -*-

from ..platform.platApiBase import PLAT_API  # 執行RF時使用
import configparser
import jsonpath

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class File(PLAT_API):

    def upload_video(self,  # 上傳影片
                     plat_token=None,
                     file=None,
                     videoPathType=None,
                     ):
        self.ps.headers.update({"Content-Type": None})
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platfrom_host+"/v1/file/video",
                                data={},
                                params={
                                    "videoPathType": videoPathType,
                                },
                                files=file,
                                )
        self._printresponse(response)
        return response.json()

    def upload_image(self,  # 上傳圖片
                     plat_token=None,
                     file=None,
                     imagePathType=None  # 1:game|2:activity|3:avatar
                     ):
        self.ps.headers.update({"Content-Type": None})
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platfrom_host+"/v1/file/image",
                                data={},
                                params={
                                    "imagePathType": imagePathType,
                                },
                                files=file,
                                )
        self._printresponse(response)
        return response.json()


class Avatar(PLAT_API):

    def add_avatar(self,  # 新增頭像
                   plat_token=None,
                   title=None,
                   url=None,
                   ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platfrom_host+"/v1/config/avatar",
                                json={
                                    "title": title,
                                    "url": url,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def edit_avatar(self,  # 修改頭像
                    plat_token=None,
                    title=None,
                    url=None,
                    id=None,
                    ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platfrom_host+"/v1/config/avatar",
                               json={
                                   "id": id,
                                   "title": title,
                                   "url": url,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def delete_avatar(self,  # 刪除頭像
                      plat_token=None,
                      id: str = None,
                      ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.delete(platfrom_host+"/v1/config/avatar/{}".format(id),
                                  json={},
                                  params={}
                                  )
        self._printresponse(response)
        return response.json()

    def get_avatar_one(self,  # 依頭像ID進行查詢
                       plat_token=None,
                       id: str = None,
                       ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platfrom_host+"/v1/config/avatar/{}".format(id),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_avatar(self,  # 依條件進行查詢
                   plat_token=None,
                   title=None,
                   ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platfrom_host+"/v1/config/avatars",
                               json={},
                               params={
                                   "title": title,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def get_delete_avatar(self,  # 獲取可刪除頭像
                          plat_token=None,
                          ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.get_avatar(title="待刪除頭像")
        ret = jsonpath.jsonpath(response, "$..id")
        if ret is False:
            self.add_avatar(title="待刪除頭像", url="justForTest")
            response = self.get_avatar(title="待刪除頭像")
            ret = jsonpath.jsonpath(response, "$..id")
        return ret[-1]