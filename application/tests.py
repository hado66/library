from django.test import TestCase

# Create your tests here.
# a = []
#
# b = [{}, {1: 3}, {9: [1, 2, 3]}]
#
# a = a+b
# print(a)
dic_code={1:"chinese_core",2:"cssci",3:"emphasis_journal",4:"top_journal"}
dic_cn={"chinese_core":"中文核心","cssci":"CSSCI","emphasis_journal":"重要期刊","top_journal":"顶级期刊"}

for i in dic_code.values():
    print(type(i))