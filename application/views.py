from django.shortcuts import render
from util.dbhelper import MVC_HOLDER
from util.parameter import match_parameter, parse_parameter
from util.callback import api_callback


@parse_parameter
@match_parameter({
    "type": "length[0-25]",
    "name": "length[0-25]",
}, api_callback)
def index(request, parameter):
    dic_code = {1: "chinese_core", 2: "cssci", 3: "emphasis_journal", 4: "top_journal"}
    dic_cn = {"chinese_core": "中文核心", "cssci": "CSSCI", "emphasis_journal": "重要期刊", "top_journal": "顶级期刊"}
    res = []
    if not parameter or not parameter['title']:
        """未选择任何参数"""
        return render(request, "index.html", {"res": res, "parameter": parameter, })
    if parameter['title'] and not parameter['type']:
        """仅选择title参数"""
        tables = dic_code.values()
        for table in tables:
            data = MVC_HOLDER.services[table].get_list({'name': parameter['title'] + '%'})
            table_name = table
            if data:
                for i in data:
                    i["type"] = dic_cn[table_name]
                res = res + data
    if parameter["type"]:
        data = MVC_HOLDER.services[dic_code.get(int(parameter["type"]))].get_list({'name': parameter['title'] + '%'})
        if data:
            for i in data:
                i["type"] = dic_cn[dic_code.get(int(parameter["type"]))]
            res = res + data

    return render(request, "index.html", {"res": res, "parameter": parameter, })
