#!/usr/bin/python3
import url_access
import html_parse
import time as t


def print_goods_list(info_goods):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in info_goods:
        count += 1
        print(tplt.format(count, g[0], g[1]))


tb = url_access.visit()
# 从第一页开始计算
index = 1
starter = html_parse.parseHTML(index)
info_list = []
while(True):
    try:
        starter.parsePage(
            info_list, tb.getHTML(starter.getPage())
        )
    except:
        break
    t.sleep(10)
print_goods_list(info_list)
# print(tb.getHTML())
