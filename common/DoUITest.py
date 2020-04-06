# -*- coding:utf-8 -*-
# @Time : 2020/4/6 12:40
# @Author: lup
__author__ = 'pei.lu'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 特殊的键
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver=webdriver.Chrome(executable_path=r'..\tools\chromedriver.exe')

driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
# 上传文件，找input，传文件路径值
driver.find_element_by_css_selector('input[type="file"]').send_keys(r'C:\Users\pei.lu.KINGSTAR\eclipse-workspace\before\tools\a.png')

# 模拟按特殊键
driver.find_element_by_id('kw').send_keys(Keys.ENTER)


#点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()

#找到id 为dropdown1的父元素
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link为Action的子元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
ActionChains(driver).move_to_element(menu).perform()  #action操作

# 模拟快捷键按ctrl+c
action=ActionChains(driver)
action.key_down(Keys.CONTROL) # 按下control键
action.send_keys('c')
action.key_up(Keys.CONTROL)  # 松开control键

# 执行js
js='document.querySelector("#rs > div").scrollIntoView()' # js 语法，只支持css定位选择器
driver.execute_script(js)


