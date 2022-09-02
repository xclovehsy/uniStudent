#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-14 14:42
# software: PyCharm

import pymysql


class SqlOp:
    """
    mysql数据库操作
    """

    def __init__(self):
        self.conn = None

    def __del__(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)

    def connect(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="xc",
            password="123456789",
            database="cqu_student"
        )

    def search(self, sql):
        """
        数据库查询功能
        :param sql: sql语句
        :return: 数据库中查找的数据， “-1”查询操作有异常， “0”表示执行的并非查询操作
        """
        if (sql[0] != 's') and (sql[0] != 'S'):
            return 0
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
            self.conn.rollback()
            data = -1

        cursor.close()
        self.conn.close()

        return data

    def update(self, sql):
        """

        :param sql: sql修改语句
        :return: -1表示修改失败，0表示执行的不是修改操作，1表示修改成功
        """
        if (sql[0] != 'u') and (sql[0] != 'U'):
            return 0
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            self.conn.commit()
            data = 1
        except Exception as e:
            print(e)
            data = -1
        cursor.close()
        self.conn.close()
        return data

    def delete(self, sql):
        """
        数据库删除功能
        :param sql: sql语句
        :return: 数据库中查找的数据， “-1”删除操作有异常 "1"删除操作无异常
        """
        if (sql[0] != 'd') and (sql[0] != 'D'):
            return 0
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            self.conn.commit()
            data = 1
        except Exception as e:
            print(e)
            self.conn.rollback()
            data = -1
        cursor.close()
        self.conn.close()
        return data

    def insert(self, sql):
        """
        数据库插入功能
        :param sql: sql语句
        :return: 数据库中查找的数据， “-1”插入操作有异常 "1"插入操作无异常
        """
        if (sql[0] != 'i') and (sql[0] != 'I'):
            return 0
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            self.conn.commit()
            data = 1
        except Exception as e:
            print(e)
            self.conn.rollback()
            data = -1
        cursor.close()
        self.conn.close()
        return data

    def createTable(self, sql):
        """

        :param sql: 建表的sql语句
        :return: -1表示建表失败，0表示执行的不是建表操作，1表示修改成功
        """
        if (sql[0] != 'c') and (sql[0] != 'C'):
            return 0
        self.connect()
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            self.conn.commit()
            data = 1
        except Exception as e:
            print(e)
            data = -1
        cursor.close()
        return data


def main():
    sql = SqlOp()
    # data = sql.search("select * from student where stuName = '南'")
    # stuName = '徐聪'
    # gender = 0
    # birth = '2002-03'
    # cityId = '2078'
    # proId = '2090'
    # disId = '20'
    # isReg = 0
    # stuId = '20195371'
    # res = sql.update(
    #     f"UPDATE `zrgj10`.`student` SET `stuName` = '{stuName}', `gender` = {gender}, `birth` = '{birth}', `cityId` = '{cityId}', `disId` = '{disId}', `status` = {isReg}, `proId` = '{proId}' WHERE `stuId` = {stuId}")
    # print(res)
    data = sql.update(f"UPDATE `cqu_student`.`student` SET `stuName` = '小' WHERE `stuId` = '701' AND `stuName` = '陈小春' AND `gender` = '0' AND `birth` = '1994' AND `cityId` = '5000' AND `disId` = '080902' AND `status` = '0' AND `proId` = '50' LIMIT 1")
    print(data)


if __name__ == '__main__':
    main()
