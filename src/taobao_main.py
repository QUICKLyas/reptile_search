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
options.add_experimental_option('excludeSwitches', ['enabled-automation'])
# 屏蔽保存密码提示框
prefs = {'credentials_enable_service': False,
         'prefile.password_manager_enable': False}
options.add_experimental_option('prefs', prefs)
# 反爬虫特征处理
options.add_argument('--disable-blink-features=AutomationControlled')
# 浏览器打开
driver = webdriver.Chrome(options=options)
# 代开登录页面
url = 'https://taobao.com'
driver.get(url)
driver.find_element(By.CSS_SELECTOR, '#q').send_keys("大米")
driver.find_element(
    By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button').click()
# ActionChains.move_to_element()
# 阻塞
input()
