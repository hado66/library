#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : api.py
# @Author:
# @Date  : 2020/10/30
# @Desc  :

from django.views.decorators.http import require_GET

from util.callback import api_callback
from util.parameter import parse_parameter, check_parameter
from util.result import HttpResponseCMD, Code, Message
from django.db import connection


@require_GET
@parse_parameter
@check_parameter({
    "type": "length[0-25]",
}, api_callback)
def get_year(request, parameter):
    """
    查询
    :request_mapping api/account
    :param request: HTTP请求
    :param parameter: 请求参数
    :return: 添加结果
    """
    # 执行
    dic_code = {1: "chinese_core", 2: "cssci", 3: "emphasis_journal", 4: "top_journal"}
    data=  []
    try:
        cursor = connection.cursor()
        sql = "select distinct year from "+dic_code.get(int(parameter["type"]))
        cursor.execute(sql)
        data_tuple = cursor.fetchall()
        for i in data_tuple:
            data.append(i[0])
    except Exception as e:
        print(e)
        return HttpResponseCMD(Code.system_error, Message.system_error, "").to_response()
    return HttpResponseCMD(Code.success, Message.success, data).to_response()
