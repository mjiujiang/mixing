#!/usr/bin/env python
# -*- coding: utf-8 -*-

debug = True

INSTALLED_APPS = (
    'admin',
    'home',
    # 'mobile',
)

# 数据库连接字符串，
# 元祖，每组为n个数据库连接，有且只有一个master，可配与不配slave
# 数据库密码eb26acWq16E1
DATABASE_CONNECTION = {
    'default': {
        'connections': [
            {
                'ROLE': 'master',
                'DRIVER': 'mysql+mysqldb',
                'UID': 'mixing',
                # 进过AES加密的密码，格式 aes::: + ciphertext
                'PASSWD': 'aes:::bE8FoAw36SPkANwInh2NmA==',
                'HOST': '127.0.0.1',
                'PORT': 3306,
                'DATABASE': 'mixing2020',
                'QUERY': {'charset': 'utf8'}
            },
            {
                'ROLE': 'slave',
                'DRIVER': 'mysql+mysqldb',
                'UID': 'mixing',
                # 进过AES加密的密码，格式 aes::: + ciphertext
                'PASSWD': 'aes:::bE8FoAw36SPkANwInh2NmA==',
                'HOST': '127.0.0.1',
                'PORT': 3306,
                'DATABASE': 'mixing2020',
                'QUERY': {'charset': 'utf8'}
            }
        ]
    }
}

