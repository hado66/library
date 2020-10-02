from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models
from django.db import connection

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


def index(request):
    cursor = connection.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema='library'")
    tables = cursor.fetchall()
    print(tables)

    return HttpResponse("index")


