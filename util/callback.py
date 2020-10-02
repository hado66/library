"""
错误回调
"""
from django.shortcuts import redirect

from util.result import HttpResponseCMD, Code


# 接口错误回调
def api_callback(message):
    return HttpResponseCMD(Code.parameter_error, message, "").to_response()


# 页面错误回调
def page_callback(message):
    return redirect('/error?msg=' + message)
