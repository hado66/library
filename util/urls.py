import inspect

from django.urls import path


def get_mapping(views):
    """
    使用注释内容处理view请求路径
    :param views: 待解析的view
    :return: 路由关系
    """
    urlpatterns = []
    for name, obj in inspect.getmembers(views):
        if inspect.isfunction(obj):
            for func_name, func in inspect.getmembers(obj):
                if func_name == "__doc__" and func is not None:
                    tag = ":request_mapping "
                    index = func.find(tag)
                    if index != -1:
                        func = func[index + len(tag):]
                        func = func[:func.find("\n")]
                        end_char = func[len(func) - 1]
                        if end_char != "/" and end_char != "\\":
                            func = func + "/"
                        urlpatterns.append(path(func, obj))
    return urlpatterns
