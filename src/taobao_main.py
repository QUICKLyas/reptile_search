#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests
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
url = 'https://taobao.com'
driver.get(url)
# 搜索
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#q').send_keys("大米")
driver.find_element(
    By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button').click()
# ActionChains.move_to_element()
# print(items.__len__)
# 搜索过程中使用
for index in range(1, 101):
    time.sleep(2)
    item_index = 1
    for i in range(1, 49):
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
            print(title, price, sales, location, shop_name, detail_url)
        except:
            continue
    driver.get('https://s.taobao.com/search?q=%E5%A4%A7%E7%B1%B3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230407&ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=2%2C48&s='+str(0+44*index))

# 阻塞
input()
