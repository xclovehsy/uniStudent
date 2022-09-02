#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-14 19:59
# software: PyCharm


from fastapi import APIRouter
from sql import sqlOp
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
import pandas as pd
import pandas as pd

# 构建api路由
router = APIRouter()

# 实例化sqlOp对象
operator = sqlOp.SqlOp()


@router.get("/getCountOfMWS")
async def getCountOfMWS():
    """
    获取男、女、总人数
    :return:
    """
    countM = len(operator.search("select * from student where gender =1"))
    countW = len(operator.search("select * from student where gender =0"))
    countS = len(operator.search("select * from student"))
    # print(countW)
    # print(type(countW))
    return JSONResponse(
        content={
            'countM': countM,
            'countW': countW,
            'countS': countS
        }
    )


@router.get("/isResCount")
async def isResCount():
    """
    获取注册、未注册人数
    :return:
    """
    countRes = len(operator.search("select * from student where status =1"))
    countNoRes = len(operator.search("select * from student where status=0"))
    return JSONResponse(
        content={
            'countRes': countRes,
            'countNoRes': countNoRes
        }
    )


@router.get("/disCount")
async def isResCount(code: int, msg: str):
    data = pd.DataFrame(operator.search(
        f"SELECT discipline.disName, a.count as disCount  from (SELECT COUNT(*) as 'count', student.disId FROM student GROUP BY student.disId) as a INNER JOIN discipline on discipline.disId = a.disId ORDER BY a.count DESC LIMIT 10"))
    categories = list(data["disName"])
    data = list(data["disCount"])
    return JSONResponse(
        content={
            'code': 1,
            'msg': '数据获取成功',
            "categories": categories,
            'series': [
                {
                    "name": "总人数",
                    "data": data
                }
            ]
        }
    )


@router.get("/test")
async def test():
    return JSONResponse(
        content=[
            {
                "name": "一月",
                "age": 80
            },
            {
                "name": "二月",
                "age": 50
            }
        ]

    )


@router.get("/disCountMWS")
async def disCountMWS():
    """
    专业人数 男生 女生 总人数
    :return:
    """
    disName = list(pd.DataFrame(operator.search(
        f"SELECT e.`专业名` from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数` limit 5"))[
                       '专业名'])
    countM = list(pd.DataFrame(operator.search(
        f"SELECT e.`男生人数` from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数` limit 5"))[
                      '男生人数'])
    countW = list(pd.DataFrame(operator.search(
        f"SELECT e.`女生人数` from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数` limit 5"))[
                      '女生人数'])
    # data4 = data1.append(data2).append(data3)
    # print(countM)
    # print(data4)
    return JSONResponse(
        content={
            "categories": disName,
            "series": [{
                "name": "男生人数",
                "data": countM,
            }, {
                "name": "女生人数",
                "data": countW,
            }]
        }
    )

# //================================
@router.get("/getProCount")
async def getProCount():
    """
    获取各省份人数
    :return:
    """
    data = pd.DataFrame(operator.search(f"SELECT b.proName, b.count from (SELECT a.count, a.proId, address.proName from (SELECT count(*) as count, proId FROM student GROUP BY proId) as a JOIN address ON address.proId = a.proId) as b GROUP BY b.proName ORDER BY b.count desc limit 7"))
    # print(data)
    return JSONResponse(
        content={
            "categories": list(data['proName']),
            "series": {
                "name": "省份",
                "data":list(data['count']),
            }
        }
    )



if __name__ == '__main__':
    # disCountMWS()
    getProCount()