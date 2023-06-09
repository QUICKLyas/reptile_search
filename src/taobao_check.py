#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests

import my_utils.file_util as fu
# 逃避检测
# 隐藏信息
options = webdriver.ChromeOptions()
# 禁止自动化栏
options.add_experimental_option('excludeSwitches', ['enable-automation'])
p = r'/tmp/.com.google.Chrome.d1oUzW/Default'
# 屏蔽保存密码提示框
prefs = {'credentials_enable_service': False,
         'prefile.password_manager_enabled': False}
options.add_experimental_option('prefs', prefs)
# 反爬虫特征处理
# options.add_argument('--user-data-dir='+p)
options.add_argument('--user-data-dir='+p)
options.add_argument('--disable-blink-features=AutomationControlled')
# 浏览器打开
driver = webdriver.Chrome(options=options)
flag = True

for index in range(1, 101):
    # 检测数据是否已经存储
    goods_list = fu.readJson(path="./data/taobao/",
                             file_name="taobao"+str(index))
    if len(goods_list) != 0:

        print("next page" + str(index), "size: " + str(len(goods_list)))
        continue
    # 重新获取数据
    flag = False
    driver.get('https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230407&ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=2%2C48&s='+str(0+44*index))
    i = 1
    while(True):
        try:
            price = driver.find_element(
                By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child('+str(i)+') > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight > strong').text
            sales = driver.find_element(
                By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child('+str(i)+') > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-1.g-clearfix > div.deal-cnt').text
            title = driver.find_element(
                By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child('+str(i)+') > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-2.title').text
            # mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-2.title
            detail_url = driver.find_element(
                By.CSS_SELECTOR, '#J_Itemlist_TLink_639012769327').get_attribute('href')
            # J_Itemlist_TLink_639012769327
            shop_name = driver.find_element(
                By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child('+str(i)+') > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a > span:nth-child(2)').text
            # mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.shop > a > span:nth-child(2)
            location = driver.find_element(
                By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child('+str(i)+') > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.location').text
            # mainsrp-itemlist > div > div > div:nth-child(1) > div:nth-child(1) > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew > div.row.row-3.g-clearfix > div.location
            # print(title, price, sales, location, shop_name, detail_url)

        except:
            print("error")
            break
        item_dict = {
            "title": title,
            "price": price,
            "sales": sales,
            "location": location,
            "shop_name": shop_name,
            "detail_url": shop_name
        }
        goods_list.append(item_dict)
        i += 1

    fu.writeJson(goods_list, path="./data/taobao/",
                 file_name="taobao"+str(index))
    time.sleep(10)
if(flag == True):
    print("OK")
else:
    print("have more try")
