#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-14 15:40
# software: PyCharm
import random

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from op import studentOp

# 构建api路由
router = APIRouter()
stuOp = studentOp.StudentOp()


@router.get('/collectInfo')
async def collectInfo(stuName: str, gender: str, birth: str, addType: int, addName: str, disName: str, isReg: int,
                      stuId: int):
    """
    学生信息录入
    :param stuName: 学生姓名
    :param gender: 性别
    :param birth: 出生年
    :param addName: 居住地址
    :param disName: 专业名
    :param isReg: 是否注册
    :return:
    """
    # gender = (gender == '男') ? 1:
    # print(gender)
    # print("test " + gender)
    # print(type(gender))
    if gender == '男':
        gender = 1
    else:
        gender = 0
    print(gender)
    code = 0
    msg = ''

    # 1表示上传成功 2地区名有误 3专业名有误 4同专业同地区同名上传失败 -1表示其他问题
    res = stuOp.collectInfo(stuName, gender, birth, addType, addName, disName, isReg, stuId)
    if res == 1:
        msg = '上传成功'
        code = 1
    elif res == 2:
        msg = "地区名有误"
    elif res == 3:
        msg = '专业名有误'
    elif res == 4:
        msg = "同专业同地区同名"
    else:
        msg = '其他错误'

    return JSONResponse(
        content={
            "code": code,
            "msg": msg,
        }
    )


#
# @router.get('/collectInfo_new')
# async def collectInfo_new(stuName: str, gender: int, age: int, addType: int, addName: str, disName: str):
#     """
#     学生信息录入
#     :param stuName: 学生姓名
#     :param gender: 性别
#     :param age: 年龄
#     :param addName: 居住地址
#     :param disName: 专业名
#     :return:
#     """
#     code = 0
#     msg = ''
#
#     # 1表示上传成功 2地区名有误 3专业名有误 4同专业同地区同名上传失败 -1表示其他问题
#     res = stuOp.collectInfo(stuName, gender, age, addType, addName, disName)
#     if res == 1:
#         msg = '上传成功'
#         code = 1
#     elif res == 2:
#         msg = "地区名有误"
#     elif res == 3:
#         msg = '专业名有误'
#     elif res == 4:
#         msg = "同专业同地区同名"
#     else:
#         msg = '其他错误'
#
#     return JSONResponse(
#         content={
#             "code": code,
#             "msg": msg,
#         }
#     )


# 代码更新=========================
import time
from sql import sqlOp
import random


@router.get('/uploadBarrage')
async def uploadBarrage(text: str):
    """
    上传弹幕
    :param text: 上传弹幕功能
    :return:
    """
    curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(type(curTime))

    sql = sqlOp.SqlOp()


    grade = 's' + str(random.randint(1, 4))

    # 这里数据库名需要更改
    res = sql.insert(f"INSERT INTO `cqu_student`.`barrage`(`time`, `text`, `grand`) VALUES ('{curTime}', '{text}', '{grade}')")
    if res == -1:
        code = 0
        msg = "上传失败"
    else:
        code = 1
        msg = "上传成功"

    return JSONResponse(
        content={
            "code": code,
            "msg": msg,
        }
    )

