#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: nguyenthong
    Date Created: 9/29/20
"""
import redis

HOST = "localhost"
PORT = 6379


class RedisConfig:

    @staticmethod
    def get_redis(db=0):
        return redis.Redis(host=HOST, port=PORT, db=db)
