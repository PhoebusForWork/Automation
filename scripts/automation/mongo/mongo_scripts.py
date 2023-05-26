from utils.database_utils import Mongo

# 測試案例"edit_lockStatus"測試鎖定預設user002為指定目標
def setup_lock_status_user():
    setup = Mongo(platform='plt')
    setup.specify_db('plt_user')
    setup.specify_collection('vs_user')

    filter_query = {"username": "user002"}
    update_query = {"$set": {"lock_status": {"LOGIN": True, "RECHARGE": True, "WITHDRAW": True, "TRANSFER": True}}}
    setup.update_one(filter_query, update_query)