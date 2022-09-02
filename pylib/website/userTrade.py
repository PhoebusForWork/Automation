from ..website.webApiBase import WEB_API #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini') #在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class userTrade(WEB_API):    #用戶-安全中心

    def balanceHistory(self,     #查詢資金明細
                    webUid = None,
                    webToken = None,
                    orderType = "",
                    startTime = "",
                    endTime = "",
                    status = "-1",
                    page = "",
                    size = "",
                    ):
        if webUid != None :
            self.ws.headers.update({"uid":str(webUid)})
            self.ws.headers.update({"token":str(webToken)})
        response = self.ws.post(web_host+"/api/gl/balance/history/v2",
                                data = {
                                    "orderType" : orderType,
                                    "startTime" : startTime,
                                    "endTime" : endTime,
                                    "status" : status,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def historySportList(self,     #獲取用戶體育注單列表 
                    webUid = None,
                    webToken = None,
                    endTime = "2022-04-01 23:59:59",
                    startTime = "2022-04-01 23:59:59",
                    channelId = None,
                    gameId = None,
                    page = None,
                    size = None,
                    status = None,
                    ):
        if webUid != None :
            self.ws.headers.update({"uid":str(webUid)})
            self.ws.headers.update({"token":str(webToken)})
        response = self.ws.post(web_host+"/api/game/v2/history/sportList",
                                data = {
                                    "channelId" : channelId,
                                    "gameId" : gameId,
                                    "startTime" : startTime,
                                    "endTime" : endTime,
                                    "status" : status,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()