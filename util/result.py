"""
常用的返回状态码以及消息
"""
from django.http import HttpResponse

import json
from datetime import datetime


class CodeModeDTO:
    # Status code
    code = 0
    # Message body
    message = ""
    # Data volume
    data = {}

    def __init__(self, code, message, data):
        """
        Initialization status transfer tool class
        :param code: Status code
        :param message: Message body
        :param data: Data volume
        """
        self.code = code
        self.message = message
        self.data = data

    def to_json(self):
        """
        Convert to JSON object
        :return:
        """
        self.data = self._parse_time(self.data)
        return json.dumps({
            "code": self.code,
            "message": self.message,
            "data": self.data
        }, ensure_ascii=False)

    def _parse_time(self, data):
        """
        Recursive processing time format
        :param data: Data to be processed
        :return: Processing result
        """
        if isinstance(data, datetime):
            data = data.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(data, tuple) or isinstance(data, list):
            for i in range(0, len(data)):
                data[i] = self._parse_time(data[i])
        if isinstance(data, dict):
            for key in data.keys():
                data[key] = self._parse_time(data[key])
        return data


class Code:
    # 查询成功
    success = 0
    # 系统内部错误
    system_error = 1
    # 参数错误
    parameter_error = 2


class Message:
    success = "查询成功"
    system_error = "系统内部错误"
    parameter_error = "参数错误"


class HttpResponseCMD(CodeModeDTO):
    """
    继承自CodeModeDTO，简化接口返回操作
    """

    def __init__(self, code, message, data):
        super().__init__(code, message, data)

    def to_response(self):
        return HttpResponse(self.to_json(), content_type="application/json,charset=utf-8")
