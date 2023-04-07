import re


class parseHTML(object):
    def __init__(self, page: int) -> None:
        self.page = page
        pass

    def parsePage(info_list, html):
        print(html)
        try:
            re1 = re.compile(r'\"view_price\"\:\"[\d\.]*\"')  # 编译商品价格正则表达式
            re2 = re.compile(r'\"raw_title\"\:\".*?\"')  # 编译商品名称正则表达式
            plt = re1.findall(html)
            tlt = re2.findall(html)
            # plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
            # tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
            for i in range(len(plt)):
                # 去掉view_price字段，只要价格部分，eval将获取到的最外层/内层的单引号或双引号去掉
                price = eval(plt[i].split(':')[1])
                title = eval(tlt[i].split(':')[1])  # 去掉raw_title字段，只要名称部分
                info_list.append([price, title])
        except:
            print("Web page parsing failed")

    def print_goods_list(self, info_goods):
        tplt = "{:4}\t{:8}\t{:16}"
        print(tplt.format("序号", "价格", "商品名称"))
        count = 0
        for g in info_goods:
            count += 1
            print(tplt.format(count, g[0], g[1]))

    def setPage(self, page: int):
        self.page = page

    def getPage(self) -> int:
        return self.page
