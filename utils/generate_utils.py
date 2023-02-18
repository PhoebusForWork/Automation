import random
import time
import string


class Make:

    @staticmethod
    def name(namelen=8):
        return ''.join(random.choice(string.ascii_letters + string.digits)
                       for _ in range(namelen))

    @staticmethod
    def mobile():
        return "1{}{}".format(random.choice('589'), ''.join(
            random.choice(string.digits) for x in range(9)))

    @staticmethod
    def date(status):
        if status == 'start':
            return time.strftime('%Y-%m-%d', time.localtime()) + 'T00:00:00Z'

        elif status == 'end':
            return time.strftime('%Y-%m-%dT', time.localtime()) + '23:59:59Z'

        else:
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
