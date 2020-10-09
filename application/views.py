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
    "title": "length[0-25]",
    "type": "range[0-999999]",
    "year": "range[0-999999]",
}, api_callback)
def index(request, parameter):
    import time
    if not parameter or not parameter['title']:
        return render(request, "index.html")
    start = time.time()
    cursor = connection.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema='library'")
    tables = cursor.fetchall()
    res = []
    for table in tables:
        data = MVC_HOLDER.services[table[0]].get_list({'name': parameter['title'] + '_%_'})
        if data:
            res = res + data
    print(time.time() - start)
    print(res)
    return render(request, "index.html", {"res": res})
