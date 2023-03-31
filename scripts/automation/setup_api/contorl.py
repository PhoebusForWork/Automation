from pylib.contorl.control import ControlAPI


def create_platform_and_sync():
    contorl = ControlAPI()
    contorl.add_host_platform()
    contorl.host_platform_sync_data()
