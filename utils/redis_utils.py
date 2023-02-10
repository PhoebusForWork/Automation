# -*- coding: utf-8 -*-
import redis
from utils.data_utils import EnvReader


env = EnvReader()
plt_host = env.REDIS_PLT_HOST
cs_host = env.REDIS_CS_HOST
plt_port = env.REDIS_PLT_PORT
cs_port = env.REDIS_CS_PORT
plt_password = env.REDIS_PLT_PASSWORD
cs_password = env.REDIS_CS_PASSWORD


class Redis:
    def __init__(self, platform='plt', select=None):
        self.host = None
        self.port = None
        self.password = None
        if platform == 'plt':
            self.host = plt_host
            self.port = plt_port
            self.password = plt_password
        elif platform == 'cs':
            self.host = cs_host
            self.port = cs_port
            self.password = cs_password
        else:
            raise "Platform Error"
        self.conn = redis.Redis(
            host=self.host, password=self.password, port=self.port, db=select)

    def keys(self, keyword='*'):
        target = self.conn.keys(keyword)
        return target

    def set_value(self, key, value):
        target = self.conn.set(key, value)
        return target


if __name__ == '__main__':
    set_result = Redis(platform='plt', select=3)
    set_result.conn.hset(name='MOCK::AWC', key='recheckResult', value='"UNKNOWN"'
                         )
    target = set_result.conn.hget(name='MOCK::AWC', key='recheckResult')
    print(target)
