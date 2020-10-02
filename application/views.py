from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models
from django.db import connection

# Create your views here.
def test(request):
    models.Test.objects.create(name='title')
    data = MVC_HOLDER.services["test"].get_model({"name": "test"})

    # print(MVC_HOLDER.services["test"].get_count())
    print(type(data))
    data = "动态的后端数据"
    cursor = connection.cursor()
    print(cursor.execute("select table_name from information_schema.tables where table_schema='library'"))
    print(cursor.fetchall())


    return render(request, "test/index.html", {"data": data})
