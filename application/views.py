from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models
from django.db import connection
from util.parameter import check_parameter, match_parameter, parse_parameter
from util.callback import api_callback, page_callback


# Create your views here.
def test(request):
    models.Test.objects.create(name='title')
    data = MVC_HOLDER.services["test"].get_model({"name": "test"})
    print(type(data))
    data = "动态的后端数据"
    cursor = connection.cursor()
    print(cursor.execute("select table_name from information_schema.tables where table_schema='library'"))
    x = cursor.fetchall()
    for i in x:
        print(i[0])
    return render(request, "test/index.html", {"data": data})


@parse_parameter
@match_parameter({
    "title": "length[0-200]",
    "model": "range[0-999999]",
    "address": "range[0-999999]",
    "status": "range[0-5]",
}, page_callback)
def index(request):
    cursor = connection.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema='library'")
    tables = cursor.fetchall()
    print(tables)

    return render(request, "index.html")
