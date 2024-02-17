use plt_account
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_account", "command" :"create"})
use plt_activity
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_activity", "command" :"create"})
use plt_report
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_report", "command" :"create"})
use plt_game
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_game", "command" :"create"})
use plt_proxy
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_proxy", "command" :"create"})
use plt_user
db.dropDatabase()
db.Collection_name.insert({"name" :"plt_user", "command" :"create"})
use plt-risk
db.dropDatabase()
db.Collection_name.insert({"name" :"plt-risk", "command" :"create"})
use wallet
db.dropDatabase()
db.Collection_name.insert({"name" :"wallet", "command" :"create"})

use plt_account
db.Collection_name.find()
use plt_activity
db.Collection_name.find()
use plt_report
db.Collection_name.find()
use plt_game
db.Collection_name.find()
use plt_proxy
db.Collection_name.find()
use plt_user
db.Collection_name.find()
use plt-risk
db.Collection_name.find()
use wallet
db.Collection_name.find()
