#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 徐聪
# datetime: 2022-08-16 10:58
# software: PyCharm

import sqlOp

import pandas as pd

def main():
    sql = sqlOp.SqlOp()


    # subList = ['艺术学理论类', '音乐与舞蹈学类', '戏剧与影视学类', '美术学类', '设计学类']
    # for sub in subList:
    #     data = sql.search(f"select disName from discipline where subCate = '{sub}'")
    #     data = pd.DataFrame(data)
    #     print(list(data["disName"]), end=',\n')
    data = pd.DataFrame(sql.search(f"SELECT cityName FROM address WHERE proName = '重庆市'"))
    print(list(data['cityName']))


if __name__ == '__main__':
    main()
