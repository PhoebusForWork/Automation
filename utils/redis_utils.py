# -*- coding: utf-8 -*-
import redis
from redis.sentinel import Sentinel
from utils.data_utils import EnvReader


env = EnvReader()
plt_host = env.REDIS_PLT_HOST
cs_host = env.REDIS_CS_HOST
plt_port = env.REDIS_PLT_PORT
cs_port = env.REDIS_CS_PORT
plt_sentinel_list = env.REDIS_PLT_SENTINEL_LIST
cs_sentinel_list = env.REDIS_PLT_SENTINEL_LIST
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


class RedisSentinel:
    def __init__(self, platform='plt', name='mymaster', select=None):
        if platform == 'plt':
            self.sentinel_list = plt_sentinel_list
            self.password = plt_password
        elif platform == 'cs':
            self.sentinel_list = cs_sentinel_list
            self.password = cs_password
        else:
            raise "Platform Error"
        setting = {
            'service_name': name,
            "socket_timeout": 60,
            "password": self.password,
            "db": select
        }
        self.sentinel = Sentinel(
            sentinels=self.sentinel_list, socket_timeout=60)
        self.master = self.sentinel.master_for(**setting)
        self.slave = self.sentinel.slave_for(**setting)


if __name__ == '__main__':
    set_result = Redis(platform='plt', select=3)
    set_result.conn.hset(name='MOCK::AWC', key='recheckResult', value='"UNKNOWN"'
                         )
    target = set_result.conn.hget(name='MOCK::AWC', key='recheckResult')
    print(target)
