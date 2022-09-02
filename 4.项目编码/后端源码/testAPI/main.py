#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-12 14:07
# software: PyCharm

# 容器
import uvicorn
# FASTAPI模板
from fastapi import FastAPI
# 配置跨域
from starlette.middleware.cors import CORSMiddleware
# 返回json格式的数据
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from api import user
from api import manager
from api import student
from api import plane
from api import dataPlane
from api import capacity

# 声明fastapi的实例
app = FastAPI()
# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 注册api模块
app.include_router(user.router, prefix="/user")
app.include_router(manager.router, prefix="/manager")
app.include_router(student.router, prefix="/student")
app.include_router(plane.router, prefix="/plane")
app.include_router(dataPlane.router, prefix='/dataPlane')
app.include_router(capacity.router, prefix='/capacity')

# 配置容器启动相应的实例
if __name__ == '__main__':
    uvicorn.run(app='main:app', port=10085, reload=True)
