# -*- coding: utf-8 -*-
from utils.generate_utils import Make
from datetime import datetime
from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
import jsonpath
import random
import string


env = EnvReader()
platform_host = env.PLATFORM_HOST


class Game(PlatformAPI):
    # 獲取遊戲列表
    def get_game_list(self, plat_token=None, gameType=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game",
            "params": {"gameType": gameType}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲設置
    def edit_game(
            self, plat_token=None,
            gameCode="必填字串", name="必填字串",
            gameDesc="必填字串", gameDetail="必填字串"*25, gameIntro="必填字串"*25,
            fee=[{"gameType": 6, "fee": 0}],
            returnPrize=0, isHot=None, isTesting=None, isNewArrival=None, isHit=None,
            hotLevel=None, sort=0, navImg="必填字串", navHoverImg="必填字串", mbImg="必填字串", hotImg=None,
            largeHotImg=None, mbGameImg="必填字串", mbHotImg="必填字串", icon="必填字串", mainIntroImg="必填字串",
            mainIntroVideo=None, subIntroImgs=["string"],
            maintainBufferStartTime='2022-01-01T00:00:00Z', maintainBufferEndTime='2022-01-01T00:00:00Z',
            maintainStartTime='2022-01-01T00:00:00Z', maintainEndTime='2022-01-01T00:00:00Z',
            maintainRemark=None, walletImg="必填字串"
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲開啟/關閉狀態
    def edit_game_status(self, plat_token=None,
                         game_code=None,
                         status=None,
                         currency=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/game/{game_code}/status",
            "params": {"status": status,
                       "currency": currency}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲開啟/關閉狀態
    def edit_game_isTesting(self, plat_token=None, game_code=None, isTesting=None, currency=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/game/{game_code}/isTesting",
            "params": {"isTesting": isTesting, "currency": currency}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 同步遊戲數據
    def game_sync(self, plat_token=None, game_code=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/game/sync",
            "params": {"gameCode": game_code}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢注單
    def get_game_orders(
            self, plat_token=None,
            startBetTime=None, endBetTime=None,
            startPayoutTime=None, endPayoutTime=None,
            minBetAmount=None, maxBetAmount=None,
            minProfit=None, maxProfit=None,
            gameCode=["AWC_LIVE_SEXY"], gameType=None,
            username=None, parentName=None, merUsername=None,
            orderId=None, status=None, merOrderId=None, isValidOrder=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/game/orders",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲平台下拉選單
    def get_game_code(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/code"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得遊戲平台查詢條件的下拉選單
    def get_game_channel_map_list(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/channel/mapList"
        }

        response = self.send_request(**request_body)
        return response.json()

    def get_game_pay_out(
            self, plat_token=None,
            username=None, channelCode=None, remark=None,
            minAmount=None, maxAmount=None,
            startTime='2022-01-01T00:00+08:00', endTime='2023-01-01T00:00+08:00',
            page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/payOut",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 調整遊戲類型
    def put_game_type(self, ):
        request_body = {
            "method": "put",
            "url": f"/v1/game/type",
            "json": {"gameTypes": [{"gameType": "SPORT", "sort": 2}, {"gameType": "LIVE", "sort": 1}, {"gameType": "ESPORT", "sort": 3}, {"gameType": "LOTTERY", "sort": 4}, {"gameType": "CARDS", "sort": 5}, {"gameType": "GAMING", "sort": 6}]}
        }
        response = self.send_request(**request_body)
        print(response)
        return response.json()


class RebateTemplate(PlatformAPI):
    # 獲取返水模板配置
    def get_template_config(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/rebate/template/config"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增返水模板配置
    def add_template_config(
            self, plat_token=None,
            templateName=None, gameType=1, betAmount=0,
            vipId=0, vipName="string", rebateRatio=0
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/rebate/template/config",
            "json": {"templateName": templateName, "gameType": gameType, "rebateConfig": [{"betAmount": betAmount, "vipLevelRebateConfig": [{"vipId": vipId, "vipName": vipName, "rebateRatio": rebateRatio}]}]}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯返水模板配置
    def edit_template_config(
            self, plat_token=None, templateId=1,
            templateName=None, gameType=None, betAmount=None,
            vipId=None, vipName=None, rebateRatio=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/rebate/template/{templateId}/config",
            "json": {"templateName": templateName, "gameType": gameType, "rebateConfig": [{"betAmount": betAmount, "vipLevelRebateConfig": [{"vipId": vipId, "vipName": vipName, "rebateRatio": rebateRatio}]}]}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除返水模板配置
    def delete_template_config(self, plat_token=None, template_id=1):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/rebate/template/{template_id}/config"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 依遊戲類型分類獲取所有返水模板
    def get_template_all_by_game_type(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/rebate/template/allByGameType"
        }

        response = self.send_request(**request_body)
        return response.json()

    def get_exist_template_auto(self, plat_token=None):
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


class GameRebate(PlatformAPI):
    # 獲取指定遊戲類型返水模板配置
    def get_game_rebate_config(self, plat_token=None, game_type=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/game/rebate/{game_type}/config"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增/編輯遊戲類型返水模板配置
    def edit_game_rebate_config(self, plat_token=None, id=None, gameCode="string", templateIds=[1]):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/game/rebate/config",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 手動結算反水
    def game_rebate_manual_rebate(self, plat_token=None, from_time="2022-09-28T00:00:00Z"):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/game/rebate/manual/rebate",
            "params": {"from": from_time}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲反水開關
    def edit_game_rebate_config_open(self, plat_token=None, open=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/game/rebate/config/open",
            "params": {"open": open}
        }

        response = self.send_request(**request_body)
        return response.json()


class RebateRecord(PlatformAPI):
    # 獲取反水紀錄
    def get_record(
            self, plat_token=None,
            settlementDateStart=None, settlementDateEnd=None,
            minRebate=None, maxRebate=None,
            minEffectiveBet=None, maxEffectiveBet=None,
            parentName=None, username=None,
            vipName=None, gameCode=None,
            page=None, size=None,
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/rebate/record",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class GameRecover(PlatformAPI):

    def get_game_recover(self,  # 獲取資金歸集審核列表
                         plat_token=None, From=None,
                         to=None, creator=None,
                         approver=None, status=None,
                         currency=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "get",
            "url": "/v1/game/recover",
            "params": {"from": From, "to": to, "status": status}
        }
        response = self.send_request(**request_body)
        return response.json()

    def post_game_recover(self,  # 一鍵歸集
                          plat_token=None, channelCode="AI",
                          gameCode="AI_SPORT_AI", currency=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "post",
            "url": "/v1/game/recover",
            "json": {"channelCode": channelCode, "gameCode": gameCode, "currency": currency}
        }
        response = self.send_request(**request_body)
        return response.json()

    def find_recover_manage_id(self, plat_token=None, status=0):
        response = self.get_game_recover(plat_token=plat_token, status=status, to=Make.date(status="end"), From=Make.date(status="start"))
        recover_manage_id = jsonpath.jsonpath(response, "$..id")
        if recover_manage_id:
            return str(recover_manage_id[-1])
        else:
            return False

    def post_game_recover_first(self,  # 資金歸集一審
                          plat_token=None, recoverManageId=None, isApprove=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "post",
            "url": "/v1/game/recover/first",
            "json": {"recoverManageId": recoverManageId, "isApprove": isApprove}
                        }
        response = self.send_request(**request_body)
        return response.json()

    def post_game_recover_second(self,  # 資金歸集二審
                          plat_token=None, recoverManageId=None, isApprove=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "post",
            "url": "/v1/game/recover/second",
            "json": {"recoverManageId": recoverManageId, "isApprove": isApprove}
        }
        response = self.send_request(**request_body)
        return response.json()

    def make_recover_status_data(self, plat_token=None, status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        if status == 'USD':
            self.post_game_recover(plat_token=plat_token, currency="USD")
        elif status == 'USDT_TRC20':
            self.post_game_recover(plat_token=plat_token, currency="USDT_TRC20")
        elif status == 'USDT_ERC20':
            self.post_game_recover(plat_token=plat_token, currency="USDT_ERC20")
            manage_id = self.find_recover_manage_id(plat_token=plat_token, status=0)
            return manage_id
        elif status in [0, 1, 3]:
            self.post_game_recover(plat_token=plat_token, currency="CNY")
            manage_id = self.find_recover_manage_id(plat_token=plat_token, status=0)
            if status == 1:
                self.post_game_recover_first(plat_token=plat_token, recoverManageId=manage_id, isApprove=True)
            elif status == 3:
                self.post_game_recover_first(plat_token=plat_token, recoverManageId=manage_id, isApprove=True)
                self.post_game_recover_second(plat_token=None, recoverManageId=manage_id, isApprove=True)
            return manage_id
        else:
            return False



