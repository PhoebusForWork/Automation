# -*- coding: utf-8 -*-

from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
import jsonpath
import random
import string


env = EnvReader()
platform_host = env.PLATFORM_HOST


class Game(PlatformAPI):

    def get_game_list(self,  # 獲取遊戲列表
                      plat_token=None,
                      gameType=None,
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/game",
                               json={},
                               params={
                                   "gameType": gameType,
                               }
                               )
        self.print_response(response)
        return response.json()

    def edit_game(self,  # 遊戲設置
                  plat_token=None,
                  gameCode="必填字串", name="必填字串",
                  gameDesc="必填字串", gameDetail="必填字串"*25, gameIntro="必填字串"*25,
                  fee=[{"gameType": 6, "fee": 0}],
                  returnPrize=0, isHot=None, isTesting=None, isNewArrival=None, isHit=None,
                  hotLevel=None, sort=0, navImg="必填字串", navHoverImg="必填字串", mbImg="必填字串", hotImg=None,
                  largeHotImg=None, mbGameImg="必填字串", mbHotImg="必填字串", icon="必填字串", mainIntroImg="必填字串",
                  mainIntroVideo=None, subIntroImgs=["string"],
                  maintainBufferStartTime='2022-01-01T00:00:00Z', maintainBufferEndTime='2022-01-01T00:00:00Z',
                  maintainStartTime='2022-01-01T00:00:00Z', maintainEndTime='2022-01-01T00:00:00Z', maintainRemark=None, walletImg="必填字串"
                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/game",
                               json={
                                   "gameCode": gameCode,
                                   "name": name,
                                   "gameDesc": gameDesc,
                                   "gameDetail": gameDetail,
                                   "gameIntro": gameIntro,
                                   "fee": fee,
                                   "returnPrize": returnPrize,
                                   "isHot": isHot,
                                   "isTesting": isTesting,
                                   "isNewArrival": isNewArrival,
                                   "isHit": isHit,
                                   "hotLevel": hotLevel,
                                   "sort": sort,
                                   "navImg": navImg,
                                   "navHoverImg": navHoverImg,
                                   "mbImg": mbImg,
                                   "hotImg": hotImg,
                                   "largeHotImg": largeHotImg,
                                   "mbGameImg": mbGameImg,
                                   "mbHotImg": mbHotImg,
                                   "icon": icon,
                                   "mainIntroImg": mainIntroImg,
                                   "mainIntroVideo": mainIntroVideo,
                                   "subIntroImgs": subIntroImgs,
                                   "maintainBufferStartTime": maintainBufferStartTime,
                                   "maintainBufferEndTime": maintainBufferEndTime,
                                   "maintainStartTime": maintainStartTime,
                                   "maintainEndTime": maintainEndTime,
                                   "maintainRemark": maintainRemark,
                                   "walletImg": walletImg
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_game_status(self,  # 遊戲開啟/關閉狀態
                         plat_token=None,
                         gameCode=None,
                         status=None,
                         ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/game/{}/status".format(gameCode),
                               json={},
                               params={
            "status": status,
        }
        )
        self.print_response(response)
        return response.json()

    def edit_game_isTesting(self,  # 遊戲開啟/關閉狀態
                            plat_token=None,
                            gameCode=None,
                            isTesting=None,
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/game/{}/isTesting".format(gameCode),
                               json={},
                               params={
            "isTesting": isTesting,
        }
        )
        self.print_response(response)
        return response.json()

    def game_sync(self,  # 同步遊戲數據
                         plat_token=None,
                         gameCode=None,
                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/game/sync/{}".format(gameCode),
                                json={},
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def get_game_orders(self,  # 查詢注單
                        plat_token=None,
                        startBetTime=None, endBetTime=None,
                        startPayoutTime=None, endPayoutTime=None,
                        minBetAmount=None, maxBetAmount=None,
                        minProfit=None, maxProfit=None,
                        gameCode=["AWC_LIVE_SEXY"], gameType=None,
                        username=None, parentName=None, merUsername=None,
                        orderId=None, status=None, merOrderId=None, isValidOrder=None,
                        page=1, size=10,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/game/orders",
                                json={
                                    # "page": page,
                                    # "size": size,
                                    "startBetTime": startBetTime,
                                    "endBetTime": endBetTime,
                                    "startPayoutTime": startPayoutTime,
                                    "endPayoutTime": endPayoutTime,
                                    "minBetAmount": minBetAmount,
                                    "maxBetAmount": maxBetAmount,
                                    "minProfit": minProfit,
                                    "maxProfit": maxProfit,
                                    "gameCode": gameCode,
                                    "gameType": gameType,
                                    "username": username,
                                    "parentName": parentName,
                                    "merUsername": merUsername,
                                    "orderId": orderId,
                                    "status": status,
                                    "merOrderId": merOrderId,
                                    "isValidOrder": isValidOrder
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def get_game_code(self,  # 遊戲平台下拉選單
                      plat_token=None,
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/game/code",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_game_channel_mapList(self,  # 取得遊戲平台查詢條件的下拉選單
                                 plat_token=None,
                                 ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/game/channel/mapList",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_game_pay_out(self,
                         plat_token=None,
                         username=None,
                         channelCode=None, remark=None,
                         minAmount=None, maxAmount=None,
                         startTime='2022-01-01T00:00+08:00', endTime='2023-01-01T00:00+08:00',
                         page=None, size=None
                         ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/game/payOut",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()


class Rebate_template(PlatformAPI):

    def get_template_config(self,  # 獲取返水模板配置
                            plat_token=None,
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/rebate/template/config",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def add_template_config(self,  # 新增返水模板配置
                            plat_token=None,
                            templateName=None, gameType=1, betAmount=0,
                            vipId=0, vipName="string", rebateRatio=0
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/rebate/template/config",
                                json={"templateName": templateName, "gameType": gameType, "rebateConfig": [
                                    {"betAmount": betAmount, "vipLevelRebateConfig": [{"vipId": vipId, "vipName": vipName, "rebateRatio": rebateRatio}]}]},
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def edit_template_config(self,  # 編輯返水模板配置
                             plat_token=None,
                             templateId=1,
                             templateName=None, gameType=None, betAmount=None,
                             vipId=None, vipName=None, rebateRatio=None
                             ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/rebate/template/{}/config".format(templateId),
                               json={"templateName": templateName, "gameType": gameType, "rebateConfig": [
                                    {"betAmount": betAmount, "vipLevelRebateConfig": [{"vipId": vipId, "vipName": vipName, "rebateRatio": rebateRatio}]}]},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def delete_template_config(self,  # 刪除返水模板配置
                               plat_token=None,
                               templateId=1
                               ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.delete(platform_host+"/v1/rebate/template/{}/config".format(templateId),
                                  json={},
                                  params={}
                                  )
        self.print_response(response)
        return response.json()

    def get_template_allByGameType(self,  # 依遊戲類型分類獲取所有返水模板
                                   plat_token=None,
                                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/rebate/template/allByGameType",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_exist_template_auto(self,
                                plat_token=None,
                                ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.get_template_config()
        ret = jsonpath.jsonpath(response, "$..id")
        if ret is False:
            self.add_template_config(templateName=''.join(
                random.choice(string.ascii_letters) for _ in range(10)))
            response = self.get_template_config()
            ret = jsonpath.jsonpath(response, "$..id")
        return ret[-1]


class Game_rebate(PlatformAPI):

    def get_game_rebate_config(self,  # 獲取指定遊戲類型返水模板配置
                               plat_token=None, gameType=None,
                               ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/game/rebate/{}/config".format(gameType),
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_game_rebate_config(self,  # 新增/編輯遊戲類型返水模板配置
                                plat_token=None,
                                id=None, gameCode="string", templateIds=[1]
                                ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/game/rebate/config",
                                json=[{"id": id, "gameCode": gameCode,
                                      "templateIds": templateIds}],
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def game_rebate_manual_rebate(self,  # 手動結算反水
                                  plat_token=None,
                                  From="2022-09-28T00:00:00Z"
                                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/game/rebate/manual/rebate",
                                json={},
                                params={
                                    "from": From
                                }
                                )
        self.print_response(response)
        return response.json()

    def edit_game_rebate_config_open(self,  # 遊戲反水開關
                                     plat_token=None,
                                     open=None
                                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/game/rebate/config/open",
                               json={},
                               params={
                                   "open": open
                               }
                               )
        self.print_response(response)
        return response.json()


class RebateRecord(PlatformAPI):

    def get_record(self,  # 獲取反水紀錄
                   plat_token=None,
                   settlementDateStart=None, settlementDateEnd=None,
                   minRebate=None, maxRebate=None,
                   minEffectiveBet=None, maxEffectiveBet=None,
                   parentName=None, username=None,
                   vipName=None, gameCode=None,
                   page=None, size=None,
                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/rebate/record",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()
