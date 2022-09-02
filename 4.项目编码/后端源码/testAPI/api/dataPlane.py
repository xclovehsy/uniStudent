#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-15 13:43
# software: PyCharm

from fastapi import APIRouter
from sql import sqlOp
# 让数据以json的格式返回
from fastapi.responses import JSONResponse
import pandas as pd

# 构建api路由
router = APIRouter()

# 实例化sqlOp对象
operator = sqlOp.SqlOp()


@router.get("/getCountOfMWS")
async def getCountOfMWS():
    """
    获取男生人数、女生人数、总人数
    :return:
    """
    countM = len(operator.search("select * from student where gender =1"))
    countW = len(operator.search("select * from student where gender =0"))
    countS = len(operator.search("select * from student"))
    # print(countW)
    # print(type(countW))
    return JSONResponse(
        content=[
            {
                "countW": countW,
                "countM": countM,
                "countSum": countS
            }
        ]
    )


@router.get("/isResProportion")
async def isResProportion():
    """
    获取是否注册人数比例
    :return:
    """
    countRes = len(operator.search("select * from student where status =1"))
    countSum = len(operator.search("select * from student"))
    countNoRes = len(operator.search("select * from student where status=0"))
    # print("countRes " + str(countRes))
    # print("sum " + str(countSum))
    return JSONResponse(
        content=[
            {
                "value": float((countRes / countSum) * 100)
            }
        ]
    )


@router.get("/disCountOfStu")
async def disCountOfStu():
    """
    获取各专业人数
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT a.disCount as count, discipline.disName as disCount FROM discipline,(SELECT disId,COUNT(*) as disCount FROM student GROUP BY disId) as a WHERE discipline.disId=a.disId ORDER BY disCount DESC")
    )


@router.get("/getProCount")
async def getProCount():
    """
    获取各省份人数
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT b.proName, b.count from (SELECT a.count, a.proId, address.proName from (SELECT count(*) as count, proId FROM student GROUP BY proId) as a JOIN address ON address.proId = a.proId) as b GROUP BY b.proName ORDER BY b.count desc LIMIT 10")
    )


@router.get("/getProCount_1")
async def getProCount_1():
    """
    获取各省份人数
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT b.proName, b.count from (SELECT a.count, a.proId, address.proName from (SELECT count(*) as count, proId FROM student GROUP BY proId) as a JOIN address ON address.proId = a.proId) as b GROUP BY b.proName ORDER BY b.count desc")
    )


@router.get("/getChongQingCityCount")
async def getChongQingCityCount():
    """
    获取重庆市各区人数
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT address.cityName,a.pCount FROM(SELECT cityId,count(*)as pCount FROM student WHERE proId=50 GROUP BY cityId )as a,address WHERE address.cityId=a.cityId")
    )


@router.get("/getCityCount")
async def getCityCount():
    """
    获取各市区人数
    :return:
    """
    # data = operator.search(
    #     f"SELECT address.cityName as x,a.pCount as y FROM(SELECT cityId,count(*)as pCount FROM student WHERE proId=50 GROUP BY cityId )as a,address WHERE address.cityId=a.cityId ORDER BY pCount DESC")
    # data = data + operator.search(f"SELECT '其他' as x, count(*) as y FROM student WHERE proId!=50")

    return JSONResponse(
        content=operator.search(
            f"SELECT * FROM ( SELECT address.cityName as x,a.pCount as y FROM(SELECT cityId,count(*)as pCount FROM student WHERE proId=50 GROUP BY cityId )as a,address WHERE address.cityId=a.cityId) a UNION All SELECT '其它' as x, count(*)as y FROM student WHERE proId!=50 ORDER BY y DESC")
    )


@router.get("/mapFromTo")
async def mapFromTo():
    """
    地图迁移图数据
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT b.proName as 'from', '重庆市' as 'to' FROM (SELECT a.proId, address.proName FROM (SELECT proId FROM student GROUP BY proId) as a INNER JOIN address on address.proId = a.proId) as b GROUP BY b.proName")
    )


@router.get("/chongQingMapFromTo")
async def chongQingMapFromTo():
    """
    重庆市地图迁移图数据
    :return:
    """
    return JSONResponse(
        content=operator.search(
            f"SELECT address.cityName as 'from', '巴南区' as 'to' FROM(SELECT cityId,count(*)as pCount FROM student WHERE proId=50 GROUP BY cityId )as a,address WHERE address.cityId=a.cityId ORDER BY pCount DESC")
    )


@router.get("/disCountMWS")
async def disCountMWS():
    """
    专业人数 男生 女生 总人数
    :return:
    """
    data1 = operator.search(
        f"SELECT e.`专业名` as x , e.`男生人数` as y, 'bar1' as s from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数`")
    data2 = operator.search(
        f"SELECT e.`专业名` as x , e.`女生人数` as y, 'bar2' as s from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数`")
    data3 = operator.search(
        f"SELECT e.`专业名` as x , e.`总人数` as y, 'line1' as s from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数`")
    # print(data1 + data2 + data3)
    # data4 = data1.append(data2).append(data3)
    # print(data4)
    return JSONResponse(
        content=data1 + data2 + data3
    )


@router.get("/disCountMW")
async def disCountMW():
    """
    专业人数 男生 女生
    :return:
    """
    data1 = operator.search(
        f"SELECT discipline.disName as x,disIdCount.mCount as y, 's1' as s FROM (SELECT e.disId,e.mCount,f.wCount,e.Scount FROM (SELECT a.disId,a.Scount ,IFNULL(b.menCount,0)as mCount FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC LIMIT 10) a LEFT JOIN (SELECT disId,count(*) AS menCount FROM student WHERE gender =1 GROUP BY disId) b ON a.disId=b.disId)as e,(SELECT c.disId,c.Scount ,IFNULL(d.womenCount,0)as wCount FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC LIMIT 10) c LEFT JOIN (SELECT disId,count(*) AS womenCount FROM student WHERE gender =0 GROUP BY disId) d ON c.disId=d.disId)as f WHERE e.disId=f.disId ORDER BY Scount DESC) as disIdCount,discipline WHERE disIdCount.disId=discipline.disId ORDER BY Scount ASC")
    data2 = operator.search(
        f"SELECT discipline.disName as x,disIdCount.wCount as y, 's2' as s FROM (SELECT e.disId,e.mCount,f.wCount,e.Scount FROM (SELECT a.disId,a.Scount ,IFNULL(b.menCount,0)as mCount FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC LIMIT 10) a LEFT JOIN (SELECT disId,count(*) AS menCount FROM student WHERE gender =1 GROUP BY disId) b ON a.disId=b.disId)as e,(SELECT c.disId,c.Scount ,IFNULL(d.womenCount,0)as wCount FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC LIMIT 10) c LEFT JOIN (SELECT disId,count(*) AS womenCount FROM student WHERE gender =0 GROUP BY disId) d ON c.disId=d.disId)as f WHERE e.disId=f.disId ORDER BY Scount DESC) as disIdCount,discipline WHERE disIdCount.disId=discipline.disId ORDER BY Scount ASC")

    # f"SELECT e.`专业名` as x , e.`女生人数` as y, 's2' as s from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数`")

    return JSONResponse(
        content=data1 + data2
    )

@router.get("/disCountMWOfCaiJing")
async def disCountMWOfCaiJing():
    """
    财经学院软件学院 专业人数 男生 女生
    :return:
    """
    data1 = operator.search(
        f"SELECT discipline.disName as x,disIdCount.s1 as y, 's1' as 's' FROM (SELECT e.disId,e.s1,f.s2,e.Scount FROM (SELECT a.disId,a.Scount ,IFNULL(b.menCount,0)as s1 FROM (SELECT disId,count(*) AS Scount FROM student WHERE (disId='080904K' OR disId='080902' OR disId='080910T') GROUP BY disId ORDER BY Scount DESC) a LEFT JOIN (SELECT disId,count(*) AS menCount FROM student WHERE gender =1 GROUP BY disId) b ON a.disId=b.disId)as e,(SELECT c.disId,c.Scount ,IFNULL(d.womenCount,0)as s2 FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC) c LEFT JOIN (SELECT disId,count(*) AS womenCount FROM student WHERE gender =0 GROUP BY disId) d ON c.disId=d.disId)as f WHERE e.disId=f.disId ORDER BY Scount DESC) as disIdCount,discipline WHERE disIdCount.disId=discipline.disId ORDER BY Scount ASC")
    data2 = operator.search(
        f"SELECT discipline.disName as x,disIdCount.s2 as y, 's2' as 's' FROM (SELECT e.disId,e.s1,f.s2,e.Scount FROM (SELECT a.disId,a.Scount ,IFNULL(b.menCount,0)as s1 FROM (SELECT disId,count(*) AS Scount FROM student WHERE (disId='080904K' OR disId='080902' OR disId='080910T') GROUP BY disId ORDER BY Scount DESC) a LEFT JOIN (SELECT disId,count(*) AS menCount FROM student WHERE gender =1 GROUP BY disId) b ON a.disId=b.disId)as e,(SELECT c.disId,c.Scount ,IFNULL(d.womenCount,0)as s2 FROM (SELECT disId,count(*) AS Scount FROM student GROUP BY disId ORDER BY Scount DESC) c LEFT JOIN (SELECT disId,count(*) AS womenCount FROM student WHERE gender =0 GROUP BY disId) d ON c.disId=d.disId)as f WHERE e.disId=f.disId ORDER BY Scount DESC) as disIdCount,discipline WHERE disIdCount.disId=discipline.disId ORDER BY Scount ASC")

    # f"SELECT e.`专业名` as x , e.`女生人数` as y, 's2' as s from (SELECT discipline.disName as 专业名,d.男生人数,d.女生人数,d.总人数 from (SELECT b.disId as 专业代号,b.男生人数,c.女生人数,(b.男生人数+c.女生人数)as 总人数 from (SELECT * FROM (SELECT disId,gender,COUNT(*) as 男生人数 FROM student GROUP BY gender,disId)as a WHERE gender=1) as b,(SELECT * FROM (SELECT disId,gender,COUNT(*) as 女生人数 FROM student GROUP BY gender,disId)as a WHERE gender=0)as c WHERE b.disId=c.disId) as d,discipline WHERE discipline.disId=d.专业代号 ORDER BY d.总人数 DESC LIMIT 10) as e ORDER BY e.`总人数`")

    return JSONResponse(
        content= data1 + data2
    )


@router.get("/ageDisplay")
async def ageDisplay():
    """
    年龄分布数据获取
    :return:
    """
    data = operator.search("SELECT birth as x, count(*) as y, 's1' as s FROM student  GROUP BY birth ORDER BY x")
    # print(data)
    return JSONResponse(
        content=data
    )


@router.get("/isRegCount")
async def isRegCount():
    """
    获取报道人数
    :return:
    """
    countRes = len(operator.search("select * from student where status =1"))
    countSum = len(operator.search("select * from student"))
    countNoRes = len(operator.search("select * from student where status=0"))
    # print("countRes " + str(countRes))
    # print("sum " + str(countSum))
    return JSONResponse(
        content=[
            {
                "countReg": countRes,
                "countSum": countSum,
                "countNoReg": countNoRes,
            }
        ]
    )



# if __name__ == '__main__':
#     getBarrage()

@router.get("/capCount")
async def capCount():
    """
    获取各种类型人数
    :return:
    """
    # countRes = len(operator.search("select * from student where status =1"))
    # countSum = len(operator.search("select * from student"))
    # countNoRes = len(operator.search("select * from student where status=0"))
    # print(operator.search(f"select count(*) from capacity WHERE stuType = '社会型（S）'"))

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '社会型（S）'")
    if len(data) == 0:
        countS = 0
    else:
        countS = data[0]['count']

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '企业型（E）'")
    if len(data) == 0:
        countE = 0
    else:
        countE = data[0]['count']

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '常规型（C）'")
    if len(data) == 0:
        countC = 0
    else:
        countC = data[0]['count']

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '现实型（R）'")
    if len(data) == 0:
        countR = 0
    else:
        countR = data[0]['count']

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '研究型（I）'")
    if len(data) == 0:
        countI = 0
    else:
        countI = data[0]['count']

    data = operator.search(f"select count(*) as count from capacity WHERE stuType = '艺术型（A）'")
    if len(data) == 0:
        countA = 0
    else:
        countA = data[0]['count']

    return JSONResponse(
        content=[{
            "x": "社会型（S）",
            "y": countS
        }, {
            "x": "企业型（E）",
            "y": countE
        }, {
            "x": "常规型（C）",
            "y": countC
        }, {
            "x": "现实型（R）",
            "y": countR
        }, {
            "x": "研究型（I）",
            "y": countI
        }, {
            "x": "艺术型（A）",
            "y": countA
        }
        ]
    )




@router.get("/radixMap")
async def radixMap():
    """
    获取能力雷达图人数
    :return:
    """
    data = operator.search(
        f"SELECT AVG(rateS), AVG(rateE), AVG(rateC), AVG(rateR), AVG(rateI),AVG(rateA) FROM capacity ")
    # print(data[0])
    return JSONResponse(
        content=[
            {
                "name": "社会型（S）",
                "data": data[0]['AVG(rateS)'],
                'type': 's1'
            }, {
                "name": "企业型（E）",
                "data": data[0]['AVG(rateE)'],
                'type': 's1'
            }, {
                "name": "常规型（C）",
                "data": data[0]['AVG(rateC)'],
                'type': 's1'
            }, {
                "name": "现实型（R）",
                "data": data[0]['AVG(rateR)'],
                'type': 's1'
            }, {
                "name": "研究型（I）",
                "data": data[0]['AVG(rateI)'],
                'type': 's1'
            }, {
                "name": "艺术型（A）",
                "data": data[0]['AVG(rateA)'],
                'type': 's1'
            },
        ]
    )

# if __name__ == '__main__':
#     radixMap()


# ============================弹幕功能========================
@router.get("/getBarrage")
async def getBarrage():
    """
    获取弹窗数据
    :return:
    """

    return JSONResponse(
        content=operator.search(f"select text, grand as s from barrage ORDER BY time LIMIT 50")
    )
