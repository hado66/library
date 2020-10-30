from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models
from django.db import connection
from util.parameter import check_parameter, match_parameter, parse_parameter
from util.callback import api_callback, page_callback


# Create your views here.
@parse_parameter
@match_parameter({
    "title": "length[0-25]",
    "type": "range[0-999999]",
    "year": "range[0-999999]",
}, api_callback)
def test(request, parameter):
    models.Test.objects.create(name='title')
    # data = MVC_HOLDER.services["test"].get_list({"name": "test"})
    # print(type(data))
    # print(data)
    data = "动态的后端数据"
    cursor = connection.cursor()
    # print(cursor.execute("select table_name from information_schema.tables where table_schema='library'"))
    # x = cursor.fetchall()
    # for i in x:
    #     print(i[0])
    return render(request, "test/index.html", {"data": data})


@parse_parameter
@match_parameter({
    "type": "length[0-25]",
    "name": "length[0-25]",
    "year": "length[0-25]",
}, api_callback)
def index(request, parameter):
    res = []
    if not parameter or not parameter['title']:
        return render(request, "index.html",{"res": res, "parameter": parameter, })

    if parameter["type"]:
        res = MVC_HOLDER.services[parameter["type"]].get_list({'name': parameter['title'] + '%'})



    cursor = connection.cursor()
    # cursor.execute("select table_name from information_schema.tables where table_schema='library'")
    # tables = cursor.fetchall()
    # #
    # #
    # #
    # for table in tables:
    #     data = MVC_HOLDER.services[table[0]].get_list({'name': parameter['title'] + '%'})
    #     print(table[0])
    #     if data:
    #         res = res + data
    # print(res)
    print(res)
    return render(request, "index.html", {"res": res, "parameter": parameter, })
    return HttpResponse("ok")
