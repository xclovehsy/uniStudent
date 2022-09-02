#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-18 11:29
# software: PyCharm
import math

from fastapi import APIRouter
from sql import sqlOp
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np

# 构建api路由
router = APIRouter()

# 实例化sqlOp对象
operator = sqlOp.SqlOp()


@router.get("/getStuInfo")
async def getStuInfo(stuId: str):
    """
    获取学生信息
    :return:
    """
    data = operator.search(f"select stuName from student where stuId = {stuId}")
    # print("data = " + data)

    # print(data)
    code = 0
    msg = ''
    name = ''
    if len(data) > 0:
        code = 1
        msg = '查找成功'
        name = data[0]['stuName']
    else:
        code = 0
        msg = '请先填写个人信息, 点击跳转'
        name = 'null'

    return JSONResponse(
        content={
            'code': code,
            'msg': msg,
            'name': name
        }
    )


@router.get("/CapAss")
def CapAss(stuId: str, value1: int, value2: int, value3: int, value4: int, value5: int, value6: int, value7: int,
           value8: int, value9: int, value10: int, value11: int, value12: int, value13: int, value14: int,
           value15: int, value16: int, value17: int, value18: int):
    """
    学生能力测试
    :return: code: 0 表示查询失败 1表示查询成功
    """

    code = 0
    msg = ""
    stuName = ""
    stuCity = ""
    stuDis = ""

    # 判断学号是否填写
    if stuId == "":
        # print("需要填写学号")
        return JSONResponse(
            content={
                "code": 0,
                "msg": "请填写学号",
                "gender":-1,
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )

    # 获取学生的个人信息
    data = operator.search(
        f"SELECT b.stuName,discipline.fieldsDis,discipline.subCate,discipline.disName,b.proName,b.cityName FROM(SELECT a.disId,a.stuName,address.cityName,address.proName from address,(SELECT disId,stuName,cityId,proId FROM student WHERE stuId = {stuId}) AS a WHERE address.cityId=a.cityId)AS b,discipline WHERE b.disId=discipline.disId")

    if len(data) == 0:
        return JSONResponse(
            content={
                "code": 0,
                "msg": "请先填写个人信息",
                "gender": -1,
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )

    # 获取学生的个人信息
    stuName = data[0]['stuName']
    cityName = data[0]["cityName"]
    proName = data[0]["proName"]
    stuCity = proName + " " + cityName
    fieldsDis = data[0]["fieldsDis"]
    subCate = data[0]["subCate"]
    disName = data[0]["disName"]
    stuDis = fieldsDis + " " + subCate + " " + disName

    # 获取学生性别
    gender = operator.search(f"select * from student where stuId = {stuId}")[0]['gender']

    # 计算评分
    rateS = float(value1 + value2 + value3) / 3
    rateE = float(value4 + value5 + value6) / 3
    rateC = float(value7 + value8 + value9) / 3
    rateR = float(value10 + value11 + value12) / 3
    rateI = float(value13 + value14 + value15) / 3
    rateA = float(value16 + value17 + value18) / 3

    maxRate = max(rateS, rateE, rateC, rateR, rateI, rateA)

    stuType = ''
    stuTrait = ''
    if rateS == maxRate:
        stuType = '社会型（S）'
        stuTrait = '喜欢与人交往、不断结交新的朋友、善言谈、愿意教导别人。关心社会问题、渴望发挥自己的社会作用。寻求广泛的人际关系，比较看重社会义务和社会道德。'
    elif rateE == maxRate:
        stuType = '企业型（E）'
        stuTrait = '追求权力、权威和物质财富，具有领导才能。喜欢竞争、敢冒风险、有野心、抱负。为人务实，习惯以利益得失，权利、地位、金钱等来衡量做事的价值，做事有较强的目的性。'
    elif rateC == maxRate:
        stuType = '常规型（C）'
        stuTrait = '尊重权威和规章制度，喜欢按计划办事，细心、有条理，习惯接受他人的指挥和领导，自己不谋求领导职务。喜欢关注实际和细节情况，通常较为谨慎和保守，缺乏创造性，不喜欢冒险和竞争，富有自我牺牲精神。'
    elif rateR == maxRate:
        stuType = '现实型（R）'
        stuTrait = '愿意使用工具从事操作性工作，动手能力强，做事手脚灵活，动作协调。偏好于具体任务，不善言辞，做事保守，较为谦虚。缺乏社交能力，通常喜欢独立做事。'
    elif rateI == maxRate:
        stuType = '研究型（I）'
        stuTrait = '思想家而非实干家,抽象思维能力强，求知欲强，肯动脑，善思考，不愿动手。喜欢独立的和富有创造性的工作。知识渊博，有学识才能，不善于领导他人。考虑问题理性，做事喜欢精确，喜欢逻辑分析和推理，不断探讨未知的领域。'
    elif rateA == maxRate:
        stuType = '艺术型（A）'
        stuTrait = '有创造力，乐于创造新颖、与众不同的成果，渴望表现自己的个性，实现自身的价值。做事理想化，追求完美，不重实际。具有一定的艺术才能和个性。善于表达、怀旧、心态较为复杂。'

    # 查看数据库中是否有数据
    data = operator.search(f"SELECT * from capacity where stuId = '{stuId}'")
    if len(data) == 0:
        # 向数据库中存储个人能力数据
        operator.insert(
            f"INSERT INTO `cqu_student`.`capacity`(`stuId`, `stuType`, `rateS`, `rateE`, `rateC`, `rateR`, `rateI`, `rateA`, `stuTrait`) VALUES ('{stuId}', '{stuType}', {rateS}, {rateE}, {rateC}, {rateR}, {rateI}, {rateA}, '{stuTrait}')")
    else:
        # print("test")
        # 更新个人能力数据
        operator.update(
            f"UPDATE `cqu_student`.`capacity` SET `stuType` = '{stuType}', `rateS` = {rateS}, `rateE` = {rateE}, `rateC` = {rateC}, `rateR` = {rateR}, `rateI` = {rateI}, `rateA` = {rateA}, `stuTrait` = '{stuTrait}' WHERE `stuId` = '{stuId}'")

    return JSONResponse(
        content={
            "code": 1,
            "msg": "评估成功",
            "gender": gender,
            "stuName": stuName,
            "stuCity": stuCity,
            "stuId": stuId,
            "stuDis": stuDis,
            "data": {
                "stuType": stuType,
                "stuTrait": stuTrait,
                "trait": {
                    "categories": [
                        "社会型（S）",
                        "企业型（E）",
                        "常规型（C）",
                        "现实型（R）",
                        "研究型（I）",
                        "艺术型（A）"
                    ],
                    "series": [
                        {
                            "name": "能力测试",
                            "data": [
                                rateS,
                                rateE,
                                rateC,
                                rateR,
                                rateI,
                                rateA,
                            ]
                        }
                    ]
                }
            }
        }
    )


@router.get("/getStuCapAss")
def getStuCapAss(stuId: str, name: str):
    """
    获取学生能力测试结果
    :return: code 0没有填写信息，1填写信息有误，2没有上传学生信息 3没有能力测试数据 4查询成功
    """

    # 没有填写信息
    if stuId == '' or name == '':
        return JSONResponse(
            content={
                "code": 0,
                "gender": -1,
                "msg": "请先填写学号和姓名",
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )
    # 没有上传学生信息
    data = operator.search(f"SELECT * FROM student where stuId = {stuId}")
    # print("test")
    # print(data)
    if len(data) == 0:
        return JSONResponse(
            content={
                "code": 2,
                "gender": -1,
                "msg": "请上传学生信息",
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )

    # 填写信息有误
    if data[0]["stuName"] != name:
        # print(data[0]["stuName"])
        return JSONResponse(
            content={
                "code": 1,
                "gender": -1,
                "msg": "请填写正确的信息",
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )

    # 没有能力测试数据
    data = operator.search(f"SELECT * FROM capacity WHERE stuId = {stuId}")
    if len(data) == 0:
        return JSONResponse(
            content={
                "code": 3,
                "gender": -1,
                "msg": "请先填写能力测试数据",
                "stuName": "null",
                "stuCity": "null",
                "stuId": "null",
                "stuDis": "null",
                "data": {
                    "stuType": "null",
                    "stuTrait": "null",
                    "trait": {
                        "categories": [],
                        "series": []
                    }
                }
            }
        )

    # 获取学生的个人信息
    data = operator.search(
        f"SELECT b.stuName,discipline.fieldsDis,discipline.subCate,discipline.disName,b.proName,b.cityName FROM(SELECT a.disId,a.stuName,address.cityName,address.proName from address,(SELECT disId,stuName,cityId,proId FROM student WHERE stuId = {stuId}) AS a WHERE address.cityId=a.cityId)AS b,discipline WHERE b.disId=discipline.disId")

    # 获取学生的个人信息
    stuName = data[0]['stuName']
    cityName = data[0]["cityName"]
    proName = data[0]["proName"]
    stuCity = proName + " " + cityName
    fieldsDis = data[0]["fieldsDis"]
    subCate = data[0]["subCate"]
    disName = data[0]["disName"]
    stuDis = fieldsDis + " " + subCate + " " + disName

    # 获取学生能力数据
    data = operator.search(f"SELECT * FROM capacity WHERE stuId = {stuId}")

    # 获取评分以及兴趣特点
    rateS = data[0]["rateS"]
    rateE = data[0]["rateE"]
    rateC = data[0]["rateC"]
    rateR = data[0]["rateR"]
    rateI = data[0]["rateI"]
    rateA = data[0]["rateA"]
    stuType = data[0]["stuType"]
    stuTrait = data[0]["stuTrait"]

    # 获取学生性别
    data = operator.search(f"select * from student where stuId = {stuId}")
    if data[0]['gender'] == 1:
        gender = 1
    elif data[0]["gender"] == 0:
        gender = 0
    else:
        gender = -1

    return JSONResponse(
        content={
            "code": 4,
            "gender": gender,
            "msg": "获取数据成功",
            "stuName": stuName,
            "stuCity": stuCity,
            "stuId": stuId,
            "stuDis": stuDis,
            "data": {
                "stuType": stuType,
                "stuTrait": stuTrait,
                "trait": {
                    "categories": [
                        "社会型（S）",
                        "企业型（E）",
                        "常规型（C）",
                        "现实型（R）",
                        "研究型（I）",
                        "艺术型（A）"
                    ],
                    "series": [
                        {
                            "name": "能力测试",
                            "data": [
                                rateS,
                                rateE,
                                rateC,
                                rateR,
                                rateI,
                                rateA,
                            ]
                        }
                    ]
                }
            }
        }
    )
