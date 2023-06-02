# -*- coding: utf-8 -*-
import time
from scripts.automation.postgres import postgres_scripts
from scripts.automation.mongo import mongo_scripts
from scripts.automation.setup_api import platform, client_side
from utils.xxl_job_utils import XxlJobs


# ####################
#  postgres-總控模擬  #
# ####################
# setting預設的站點資料
postgres_scripts.edit_the_default_platform()
# 這邊要進行plt-basic的sync
XxlJobs.sync_plt_basics_data()
wait_for_sync = 5
time.sleep(wait_for_sync)

# #############
#  API 預處理  #
# #############

platform.super_admin_initialize()
platform.create_dept_and_role()
platform.create_account()
platform.login_account()
platform.turn_on_the_game_to_test()
client_side.create_initial_user()

# #############
#   postgres  #
# #############

postgres_scripts.host_platform()
postgres_scripts.plt_account()
postgres_scripts.plt_game()
postgres_scripts.wallet()
platform.sync_relation_manage()

# #############
#    mongo    #
# #############

mongo_scripts.setup_lock_status_user() # 有問題
