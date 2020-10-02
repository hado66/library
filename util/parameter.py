import os
from datetime import datetime
from functools import wraps

from util.verification import verification

from opering.settings import BASE_DIR, BASE_HOST, STATIC_URL
from util.uuid import get_uuid


def parse_parameter(func):
    """
    参数解析
    :param func: view方法
    :return: wrap
    """
    @wraps(func)
    def wrap(request, *args, **kwargs):
        """
        解析parameter参数
        :param request: HTTP请求
        :param args: 参数元组
        :param kwargs: 参数字典
        :return: view方法返回值
        """
        # 提取参数
        parameter = _parse_parameter(request)
        return func(request, parameter, *args, **kwargs)
    return wrap


def _parse_parameter(req):
    """
    简单读取请求中的参数，不包含JSON，POST优先
    :param req: 请求体
    :return: 参数字典
    """
    # 初始化返回值
    result = {}
    for item in req.GET:
        result[item] = "".join(req.GET[item])
    for item in req.POST:
        result[item] = "".join(req.POST[item])
    return result


def save_file(config):
    """
    文件保存装饰器
    {
        "file": "file_input_name",
        "mime": "image/*",
        "size": "65525",
    }
    :param config: 文件限制
    :return: wrap
    """
    @wraps(config)
    def wrap(func):
        """
        内嵌装饰器
        :param func: view方法
        :return: inner_wrap
        """
        @wraps(func)
        def inner_wrap(request, parameter, *args, **kwargs):
            """
            校验parameter参数
            :param request: HTTP请求
            :param parameter: 参数字典
            :param args: 参数元组
            :param kwargs: 参数字典
            :return: view方法返回值
            """
            # 提取文件
            file = request.FILES.get(config["file"])
            if file is None:
                return func(request, parameter, *args, **kwargs)
            # 格式校验
            if config["mimes"] is not None and len(config) != 0:
                flag = False
                for mime in config["mimes"]:
                    if file.content_type.startswith(mime):
                        flag = True
                if not flag:
                    return func(request, parameter, *args, **kwargs)
            if config["size"] is not None and file.size > config["size"]:
                return func(request, parameter, *args, **kwargs)
            # 保存文件
            parameter[config["file"]] = _save_file(file)
            return func(request, parameter, *args, **kwargs)
        return inner_wrap
    return wrap


def _save_file(file):
    """
    保存文件
    :param file: 文件对象
    :return: 保存路径
    """
    # 获取当前日期
    date = datetime.now().strftime("%Y-%m-%d")
    # 获取文件名
    file_name = get_uuid() + os.path.splitext(file.name)[1]
    # 目录创建
    save_path = BASE_DIR + STATIC_URL + 'upload/' + date + "/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 文件写入
    file_path = os.path.join(save_path, file_name)
    f = open(file_path, 'wb')
    for chunk in file.chunks():
        f.write(chunk)
    f.close()
    # 计算保存路径
    return BASE_HOST + STATIC_URL + 'upload/' + date + "/" + file_name


def check_parameter(config, callback):
    """
    [强校验]参数校验装饰器
    :param config: 参数校验规则
    :param callback: 校验出错回调
    :return: wrap
    """
    @wraps(config)
    def wrap(func):
        """
        内嵌装饰器
        :param func: view方法
        :return: inner_wrap
        """
        @wraps(func)
        def inner_wrap(request, parameter, *args, **kwargs):
            """
            校验parameter参数
            :param request: HTTP请求
            :param parameter: 参数字典
            :param args: 参数元组
            :param kwargs: 参数字典
            :return: view方法返回值
            """
            # 格式校验
            b, message = verification.Helper(parameter, config).check()
            if not b:
                return callback(message)
            return func(request, parameter, *args, **kwargs)
        return inner_wrap
    return wrap


def match_parameter(config, callback):
    """
    [弱校验]参数校验装饰器
    :param config: 参数校验规则
    :param callback: 校验出错回调
    :return: wrap
    """
    @wraps(config)
    def wrap(func):
        """
        内嵌装饰器
        :param func: view方法
        :return: inner_wrap
        """
        @wraps(func)
        def inner_wrap(request, parameter, *args, **kwargs):
            """
            校验parameter参数
            :param request: HTTP请求
            :param parameter: 参数字典
            :param args: 参数元组
            :param kwargs: 参数字典
            :return: view方法返回值
            """
            # 格式校验
            b, message = verification.Helper(parameter, config).weak_check()
            if not b:
                return callback(message)
            return func(request, parameter, *args, **kwargs)
        return inner_wrap
    return wrap
