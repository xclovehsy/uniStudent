#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-13 19:39
# software: PyCharm

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from op import managerOp
from op import managerOp


class Account(BaseModel):
    mgAcc: str
    psd: str
    mgName: str
    tel: str
    email: str


# 构建api路由
router = APIRouter()
magOp = managerOp.ManageOp()


@router.get('/loginService')
async def loginService(mgAcc: str, psw: str):
    """
    管理者的注册
    :param mgAcc: 账号
    :param psw: 密码
    :return:
    """
    # 1表示成功登录 2表示密码错误 3账号不存在 4账号已登录 -1表示出现异常 以及用户名
    status, name = magOp.login(mgAcc, psw)
    msg = ''
    code = 0
    if status == 1:
        code = 1
        msg = '登陆成功'
    elif status == 2:
        code = 0
        msg = '密码错误'
    elif status == 3:
        code = 0
        msg = '账号不存在'
    elif status == 4:
        code = 0
        msg = '账号已登录'
    elif status == -1:
        code = 0
        msg = '未知异常'

    return JSONResponse(
        content={
            "code": code,
            "msg": msg,
            "data": {
                "name": name,
                "avtar": "https://xc-figure.oss-cn-hangzhou.aliyuncs.com/img/202208131639176.jpg"
            }
        }
    )


# @router.get('/registerService')
# async def registerService(account: Account):
#     """
#     管理员的注册api
#     :param account: 注册账户信息
#     :return:
#     """
#     msg = ''
#     # 1表示注册成功 2 表示该账户名已存在  -1表示其他错误
#     code = magOp.register(account)
#     if code == 1:
#         msg = "注册成功"
#     else:
#         msg = "表示该账户名已存在"
#
#     return JSONResponse(
#         content={
#             "code": code,
#             "msg": msg
#         }
#     )

@router.get('/registerService')
async def registerService(mgAcc: str, psd: str, mgName: str, tel: str, email: str):
    """
    管理员的注册api
    :param account: 注册账户信息
    :return:
    """
    msg = ''
    # 1表示注册成功 2 表示该账户名已存在  -1表示其他错误
    code = magOp.register(mgAcc, psd, mgName, tel, email)
    if code == 1:
        msg = "注册成功"
    else:
        msg = "该账户已存在"

    return JSONResponse(
        content={
            "code": code,
            "msg": msg
        }
    )
