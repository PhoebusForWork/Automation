import random
import time
import string
import base64
import hashlib
import datetime


class Make:

    @staticmethod
    def name(namelen=8):
        return ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(namelen))

    @staticmethod
    def mobile():
        return "1{}{}".format(
            random.choice('589'),
            ''.join(random.choice(string.digits) for x in range(9)))

    @staticmethod
    def date(status):
        if status == 'start':
            return time.strftime('%Y-%m-%d', time.localtime()) + 'T00:00:00Z'

        elif status == 'end':
            return time.strftime('%Y-%m-%dT', time.localtime()) + '23:59:59Z'

        else:
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    @staticmethod
    def sign(os_type, SECRET, device_id=3263782594) -> dict:
        timestamp = str(int(datetime.datetime.now().timestamp()))
        pre_sign = f'device-id={device_id}&os-type={os_type}&timestamp={timestamp}{SECRET}'
        md5_sign = hashlib.md5(pre_sign.encode()).digest()
        after_sign = base64.b64encode(md5_sign).decode()
        return {"timestamp": timestamp, "sign": after_sign}
