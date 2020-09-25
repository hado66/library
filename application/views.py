from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models


# Create your views here.
def test(request):
    models.Test.objects.create(name='title')
    data = MVC_HOLDER.services["test"].get_model({"name": "test"})
    print(type(data))
    data = "动态的后端数据"
    return render(request, "test/index.html", {"data": data})
