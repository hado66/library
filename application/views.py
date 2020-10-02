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
def test(request,parameter):
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
    "title": "length[0-25]",
    "type": "range[0-999999]",
    "year": "range[0-999999]",
}, api_callback)
def index(request, parameter):
    import time
    start = time.time()
    cursor = connection.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema='library'")
    tables = cursor.fetchall()
    print(tables)
    print(parameter)
    data = MVC_HOLDER.services["center_2017"].get_first({'name': '安徽史学'})
    print(data)
    print(time.time()-start)


    return render(request, "test/index.html")
