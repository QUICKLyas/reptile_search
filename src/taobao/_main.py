#!/usr/bin/python3
import url_access
import html_parse
import time
import random
from selenium import webdriver


# def parse_data():
#     divs = driver.find_elements_by_xpath(
#         '//div[@class="grid g-clearfix"]/div/div')  # 所有的div标签

#     for div in divs:
#         test = div.find_element_by_xpath(
#             './/div[@class="row row-2 title"]/a').text  # 商品名字
#         price = div.find_element_by_xpath('.//strong').text + '元'  # 商品价格
#         deal = div.find_element_by_xpath(
#             './/div[@class="deal-cnt"]').text  # 付款人数
#         name = div.find_element_by_xpath(
#             './/div[@class="shop"]/a/span[2]').text  # 店铺名称
#         location = div.find_element_by_xpath(
#             './/div[@class="location"]').text  # 店铺地点
#         detail_url = div.find_element_by_xpath(
#             './/div[@class="row row-2 title"]/a').get_attribute('href')  # 详情页地址
#         print(test, price, deal, name, location, detail_url)


# if __name__ == '__main__':
#     word = input('请输入要搜索的关键字：')
#     # TODO 1、创建浏览器
#     driver = webdriver.Chrome()
#     # TODO 2、修改了浏览器的内部属性，跳过了登录的滑动验证
#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
#                            {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
#     # TODO 3、执行浏览器操作
#     driver.get('https://www.taobao.com/')
#     driver.implicitly_wait(10)  # 智能化等待方法
#     driver.maximize_window()  # 最大化
#     driver.find_element('//*[@id="q"]').send_keys(word)
#     time.sleep(random.randint(1, 3))
#     driver.find_element(
#         '//*[@id="J_TSearchForm"]/div[1]/button').click()
#     time.sleep(random.randint(1, 3))

#     """用户账号及密码登录"""
#     driver.find_element_by_xpath(
#         '//*[@id="fm-login-id"]').send_keys('yabuto')  # TODO 输入用户名
#     time.sleep(random.randint(1, 3))
#     driver.find_element_by_xpath(
#         '//*[@id="fm-login-password"]').send_keys('345789quickly')  # TODO 输入密码
#     time.sleep(random.randint(1, 3))
#     driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
#     time.sleep(random.randint(1, 3))
#     for page in range(0, 2):
#         print(f'-----------------正在爬取第{page + 1}页-----------------')
#         # TODO 调用商品解析的函数
#         parse_data()
#         driver.find_element_by_xpath(
#             '//li[@class="item next"]/a[@class="J_Ajax num icon-tag"]').click()
#         time.sleep(random.randint(2, 3))
# tb = url_access.visit()

# # 从第一页开始计算
# index = 1
# starter = html_parse.parseHTML(index)
# info_list = []

# while(True):
#     try:
#         print("page :", starter.getPage())
#         print(tb.getHTML(starter.getPage()))
#         starter.parsePage(
#             info_list, tb.getHTML(starter.getPage())
#         )
#     except:
#         break
#     t.sleep(10)
# starter.print_goods_list(info_list)
# print(tb.getHTML())
