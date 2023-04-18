from pylib.client_side.validation import Validation
from utils.generate_utils import Make


def create_initial_user():
    user_list = ["user001", "user002",
                 "wallet001", "wallet002",
                 "game001", "game002"]
# 6-18字下方帳號無法正常創建有bug待補
# "activity001", "activity002"]
    for user in user_list:
        pwd = 'abc123456'
        api = Validation()
        api.user_register(deviceId=Make.mobile(), username=user,
                          password=pwd, confirmPassword=pwd)
