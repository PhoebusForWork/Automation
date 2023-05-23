from pylib.client_side.validation import Validation
from pylib.client_side.test import TransferMock
from pylib.client_side.user import Security
from utils.generate_utils import Make


def create_initial_user():
    set_test_controller = TransferMock()
    set_test_controller.set_env(is_pro=False)
    user_list = ["user001", "user002",
                 "wallet001", "wallet002",
                 "game001", "game002",
                 "activity001", "activity002",
                 "status001", "status002",
                 "generic001", "generic002", "generic003", "generic004", "generic005", "generic006", "generic007", "generic008", "generic009", "generic010",
                 "generic011", "generic012", "generic013", "generic014", "generic015", "generic016", "generic017", "generic018", "generic019", "generic020",
                 "generic021", "generic022", "generic023", "generic024", "generic025", "generic026", "generic027", "generic028", "generic029", "generic030",
                 "generic031", "generic032", "generic033", "generic034", "generic035", "generic036", "generic037", "generic038", "generic039", "generic040"
                 ]
    for user in user_list:
        pwd = 'abc123456'
        api = Validation()
        api.user_register(deviceId=Make.mobile(), username=user,
                          password=pwd, confirmPassword=pwd)


def binding_mobile():
    validation_api = Validation()
    resp = validation_api.login(username='user001', password="abc123456")
    admin_token = resp.json()['data']['token']
    set_test_binding = Security(admin_token)
    set_test_binding.mobile_binding(countryCode=86, mobile=18198977777, code="000000")
