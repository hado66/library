from django.shortcuts import render, HttpResponse
from util.dbhelper import MVC_HOLDER
from application import models

# Create your views here.
def test(request):
    print("fsdafsa")
    # MVC_HOLDER.services["test"].insert({"name": "test"})
    models.Test.objects.create(name= 'title')
    # MVC_HOLDER.services["test"].insert({'name': 'ddd'})
    data = MVC_HOLDER.services["test"].get_model({"name": "test"})
    print(type(data))
    return HttpResponse("ok")
