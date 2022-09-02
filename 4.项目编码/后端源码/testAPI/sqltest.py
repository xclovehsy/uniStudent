#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-13 12:20
# software: PyCharm

import pymysql


def main():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="xc", password="123456789", database="cqu_student")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # SQL 插入语句
    stu_name = "陈龙灿"
    # sql = f"SELECT * FROM student WHERE stuName = '{stu_name}'"
    sql = f"INSERT INTO `cqu_student`.`student`(`stuNo`, `stuName`, `tNo`, `stuAge`, `"

    try:
        # 执行sql语句
        cursor.execute(sql)
        # data = cursor.fetchall()
        # 把查询的数据填充到person对象是否可以(要循环这个游标进行数据的填充)
        # 可以将查询的数据填充(组合)到自定义的模型中
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    cursor.close()
    db.close()
    # print(data)


if __name__ == '__main__':
    main()
