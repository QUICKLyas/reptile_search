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
url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.5af911d9249jSV&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
driver.get(url)
# 登录
driver.find_element(By.CSS_SELECTOR, '#fm-login-id').send_keys("18362134438")
driver.find_element(
    By.CSS_SELECTOR, '#fm-login-password').send_keys("345789quickly")
# 处理滑块
try:
    # 进入内嵌页面
    driver.switch_to.frame(0)
    slider = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
    # 鼠标操作
    webdriver.ActionChains(driver).click_and_hold(on_element=slider).perform()
    webdriver.ActionChains(driver).move_by_offset(
        xoffset=260, yoffset=0).perform()
    # 结束鼠标操作
    webdriver.ActionChains(driver).pause(0.5).release().perform()
    driver.switch_to.parent_frame()
except:
    print("There are some questions")
pass
# 阻塞
input()
