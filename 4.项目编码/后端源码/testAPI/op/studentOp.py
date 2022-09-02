#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-14 15:50
# software: PyCharm

from pydantic import BaseModel

from sql import sqlOp
import datetime


class Student(BaseModel):
    stuName: str
    gender: int
    age: int
    addName: str
    disName: str


class StudentOp:
    """学生信息登录相关操作"""

    def __init__(self):
        self.sql = sqlOp.SqlOp()

    def collectInfo(self, stuName, gender, birth, addType, addName, disName, isReg, stuId):
        """
        上传学生信息到数据库
        :param stuName: 学生姓名
        :param gender: 性别
        :param birth: 出生年月
        :param addType: 1表示省 2表示市
        :param addName: 地区名
        :param disName: 专业名
        :param isReg: 是否注册
        :param stuId: 学号
        :return: 1表示上传成功 2地区名有误 3专业名有误 4同专业同地区同名上传失败 -1表示其他问题
        """
        # print(birth)
        # print(type(birth))
        # print("----------test----")
        # 判断专业名是否正确
        disId = self.getDisName(disName)
        if disId == -1:
            print("专业名有误")
            return 3

        # 判断地区名是否有效
        proId, cityId = self.getAddrIdtest(addType, addName)
        if (proId, cityId) == (-1, -1):
            print("地区名有误")
            return 2

        # 判断同地区同专业同姓名情况
        # res = self.isSumAreaDisName(addType, proId, cityId, disId, stuName)
        # if res == 1:
        #     print("同地区同专业同姓名")
        #     return 4

        # 判断是否有 同样学号的记录
        if self.haveSameStuId(stuId) == 1:
            res = self.sql.update(f"UPDATE `cqu_student`.`student` SET `stuName` = '{stuName}', `gender` = {gender}, `birth` = '{birth}', `cityId` = '{cityId}', `disId` = '{disId}', `status` = {isReg}, `proId` = '{proId}' WHERE `stuId` = {stuId}")
            if res == -1:
                print("here===========================")
                return -1
            else:
                return 1

        else:
            # today = datetime.datetime.today()
            # 上传学生信息
            # “-1”插入操作有异常"1"插入操作无异常
            res = self.sql.insert(
                f"INSERT INTO `cqu_student`.`student`(`stuId`, `stuName`, `gender`, `birth`, `cityId`, `disId`, `status`, `proId`) VALUES ({stuId}, '{stuName}', {gender}, '{birth}', '{cityId}', '{disId}', {isReg}, '{proId}')")
            if res == -1:
                return -1
            else:
                return 1

    def haveSameStuId(self, stuId):
        """
        判断是否有相同学号的记录
        :return: 1表示有, 0表示没有
        """
        data = self.sql.search(f"SELECT * FROM student WHERE stuId = '{stuId}'")
        if len(data) > 0:
            return 1
        else:
            return 0

    def getDisName(self, disName):
        """
        获取专业代码
        :param disName: 专业名
        :return: 专业代码 如果查找失败返回-1
        """
        disId = self.sql.search(f"SELECT discipline.disId from discipline WHERE discipline.disName = '{disName}'")
        if len(disId) == 0:
            # print("专业名查找失败")
            return -1
        return disId[0]['disId']

    def getAddrId(self, addType, addName):
        """
        获取省市行政区代码
        :param addType: 地区类别（1表示省，0表示市）
        :param addName: 地区名
        :return:（省行政区代码， 市行政区代码） （-1， -1） 表示地区有误
        """
        cityId = -1
        proId = -1
        if addType == 1:
            """省名称"""
            if addName[-1] != "省":
                addName = addName + "省"

            proId = self.sql.search(f"SELECT address.proId FROM address WHERE address.proName = '{addName}'")
            if len(proId) == 0:
                print("地区名有误")
                return (-1, -1)
            proId = proId[0]['proId']
            return (proId, -1)

        elif addType == 2:
            """市名称"""
            if addName[-1] != '市':
                addName = addName + "市"
            cityId = self.sql.search(f"SELECT address.cityId FROM address WHERE address.cityName = '{addName}'")
            if len(cityId) == 0:
                print("地区名有误")
                return (-1, -1)
            cityId = cityId[0]['cityId']

            proId = self.sql.search(f"SELECT address.proId FROM address WHERE address.cityId = '{cityId}'")
            proId = proId[0]["proId"]
            return (proId, cityId)

    def getAddrIdtest(self, addType, addName):
        """
        获取省市行政区代码
        :param addType: 地区类别（1表示省，0表示市）
        :param addName: 地区名
        :return:（省行政区代码， 市行政区代码） （-1， -1） 表示地区有误
        """
        cityId = -1
        proId = -1
        if addType == 1:
            """省名称"""
            # if addName[-1] != "省":
            #     addName = addName + "省"

            proId = self.sql.search(f"SELECT address.proId FROM address WHERE address.proName = '{addName}'")
            if len(proId) == 0:
                proId = self.sql.search(f"SELECT address.proId FROM address WHERE address.proName = '{addName + '省'}'")
                if len(proId) == 0:
                    print("地区名有误")
                    return (-1, -1)

            proId = proId[0]['proId']
            return (proId, -1)

        elif addType == 2:
            """市名称"""
            # if addName[-1] != '市':
            #     addName = addName + "市"
            cityId = self.sql.search(f"SELECT address.cityId FROM address WHERE address.cityName = '{addName}'")
            if len(cityId) == 0:
                cityId = self.sql.search(
                    f"SELECT address.cityId FROM address WHERE address.cityName = '{addName + '市'}'")
                if len(cityId) == 0:
                    print("地区名有误")
                    return (-1, -1)

            cityId = cityId[0]['cityId']

            proId = self.sql.search(f"SELECT address.proId FROM address WHERE address.cityId = '{cityId}'")
            proId = proId[0]["proId"]
            return (proId, cityId)

    def isSumAreaDisName(self, addType, proId, cityId, disId, stuName):
        """
        判断是否同专业同地区同名的情况
        :param addType: 行政区类型 1表示省  2表示市
        :param proId: 省行政区id
        :param cityId: 市行政区id
        :param disId: 专业id
        :return: 1表示有同名 0表示没有同名的
        """
        if addType == 1:
            # self.sql.search(f"SELECT * FROM student WHERE student.stuName = '{stuName}' AND student.disId = '{disId}' AND student.addrId= '{addId}'")) > 0
            res = self.sql.search(
                f"SELECT * FROM student WHERE student.stuName = '{stuName}' AND student.proId = '{proId}' AND student.disId = '{disId}'")
            # print("-----------")
            # print(f"SELECT * FROM student WHERE student.stuName = '罗翔' AND student.proId = 35 AND student.disId = '030101K'")
            if type(res) == int:
                return 1

            if len(res) == 0:
                return 0
            else:
                return 1
        elif addType == 2:
            res = self.sql.search(
                f"SELECT * FROM student WHERE student.stuName = '{stuName}' AND student.cityId = '{cityId}' AND student.disId = '{disId}'")
            if len(res) == 0:
                return 0
            else:
                return 1


def main():
    # collectInfo(self, stuName, gender, age, addType, addName, disName):
    s = StudentOp()
    # s.collectInfo('a', 1, 21, 2, '沈阳市', '哲学')
    print(s.haveSameStuId(2019537))


if __name__ == '__main__':
    main()
