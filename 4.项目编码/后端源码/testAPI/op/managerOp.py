#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-13 19:39
# software: PyCharm

import pymysql
from pydantic import BaseModel

from sql import manageSql


class Account(BaseModel):
    mgAcc: str
    psd: str
    mgName: str
    tel: str
    email: str


class ManageOp:
    """管理者登录以及注册相关操作"""

    def __init__(self):
        self.magSql = manageSql.ManageSql()

    def login(self, mgAcc, psw):
        """
        管理着登录操作
        :param mgAcc: 账号
        :param psw: 密码
        :return: 1表示成功登录 2表示密码错误 3账号不存在 4账号已登录 -1表示出现异常 以及用户名
        """
        data = self.magSql.searchAllByCol('mgAcc', mgAcc)
        # print(data)
        if len(data) == 0:
            return 3, ''
        elif data[0]["psd"] == psw:
            return 1, data[0]["mgName"]
        elif data[0]["psd"] != psw:
            return 2, ''
        else:
            return -1, ''

    def register(self, mgAcc, psd, mgName, tel, email):
        """
        管理者的注册
        :param account: 账户信息
        :return:1表示注册成功 2 表示该账户名已存在  -1表示其他错误
        """
        # 判断数据库中是否已经存在
        accounts = self.magSql.searchAllByCol('mgAcc', mgAcc)

        if len(accounts) == 0:
            # 向数据库中添加账户信息
            self.magSql.addManager(mgAcc, psd, mgName, tel, email, 0)
            return 1
        else:
            return 2


def main():
    m = ManageOp()
    # print(m.login("xucong", "xucongNB123"))


if __name__ == '__main__':
    main()
