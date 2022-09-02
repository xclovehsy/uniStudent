#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-14 7:18
# software: PyCharm

import pymysql


class ManageSql:
    def __init__(self):
        self.conn = None

    def __del__(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)

    def connect(self):
        self.conn = pymysql.connect(
            host="124.222.244.117",
            user="zrgj10",
            password="zrgj10",
            database="zrgj10"
        )

    def searchAllByCol(self, col, key):
        """
        通过字段查找所有数据
        :param col: 字段
        :param key: 关键字
        :return: 数据库中查询的数据
        """
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = f"SELECT * FROM manage WHERE {col} = '{key}'"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
            data = None
            self.conn.rollback()
        cursor.close()
        self.conn.close()

        return data

    def addManager(self, mgAcc, psd, mgName, tel, email, status):
        """
        添加管理者
        :param mgAcc: 账号
        :param psd: 密码
        :param mgName: 姓名
        :param tel: 电话
        :param email: 邮箱
        :return: 1表示成功 0表示失败
        """
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = f"INSERT INTO `zrgj10`.`manage`(`mgName`, `mgAcc`, `psd`, `tel`, `email`, `status`) VALUES ('{mgName}', '{mgAcc}', '{psd}', '{tel}', '{email}', '{status}')"
        res = 0
        try:
            res = cursor.execute(sql)
            # data = cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
            res = 0
            self.conn.rollback()
        cursor.close()
        self.conn.close()

        if res >= 1:
            res = 1

        return res

    def searchAllByCol(self, key, value):
        """
        通过字段进行查询
        :param key: 字段名
        :param value: 关键字
        :return: 返回查询的数据
        """
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = f"select * from manage where {key} = '{value}'"
        data = None
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            # self.conn.commit()
        except Exception as e:
            print(e)
            data = None
            self.conn.rollback()
        cursor.close()
        self.conn.close()

        return data


def main():
    a = ManageSql()
    # print(a.addManager('xc', 'xc', 'test', 'o', 'o'))
    print(len(a.searchAllByCol('mgAcc', 'x')))


if __name__ == '__main__':
    main()
