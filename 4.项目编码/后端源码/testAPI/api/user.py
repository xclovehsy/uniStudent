#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-12 14:19
# software: PyCharm
# 引入路由管理

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
from op import studentOp


class Account(BaseModel):
    name: str
    psw: str


# 构建api路由
router = APIRouter()


@router.get("")
async def test():
    print("hello")
    return JSONResponse(
        content={
            'msg':1
        }
    )


@router.get("/loginService1")
async def loginService1(id: str, psw: str):
    print(id)
    print(psw)

    return JSONResponse(
        content={
            "code": 1,
            "msg": f"欢迎用户，登录成功！",
            "data": {
                "name": "徐聪",
                "avtar": "https://xc-figure.oss-cn-hangzhou.aliyuncs.com/img/202208131639176.jpg"
            }
        }
    )


@router.get("/loginService2")
async def loginService2(id: str, psw: str):
    # print(studentOp.selectAllStudent())
    # p1 = dict(student=studentOp.selectAllStudent())
    # return JSONResponse(
    #     content={
    #         'code': 1,
    #         'data': studentOp.selectAllStudent(),
    #         'desc': '查询数据'
    #     }
    # )
    return f"{id} 你好！"
    # return id + "你好"
