# -*- coding:utf-8 -*-
# @Time : 2020/4/6 12:40
# @Author: lup
__author__ = 'pei.lu'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 特殊的键
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains # 模拟人工动作类
from selenium.webdriver.support.select import Select # 操作select下拉框
# import baidu-ocr # 做图片验证码识别

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

# 移动到页面最后一个元素
eles=driver.find_elements_by_css_selector('XXX')
last_ele=eles[-1]
ActionChains(driver).move_to_element(eles[-1]).perform()  # action操作

last_ele.location_once_scrolled_into_view  # 属性，滚动到网页视图

# 百度首页的  更多---文库--
ActionChains(driver).move_to_element('更多定位').perform()  # perform表示执行
'文库定位'.click()

# 模拟快捷键按ctrl+c
action=ActionChains(driver)
action.key_down(Keys.CONTROL) # 按下control键
action.send_keys('c')
action.key_up(Keys.CONTROL)  # 松开control键

# action.context_click() # 右击
# action.drag_and_drop # 拖拽

# 执行js
js='document.querySelector("#rs > div").scrollIntoView()' # js 语法，只支持css定位选择器
driver.execute_script(js)

# 获取属性值
ele=driver.find_element_by_css_selector('XXX')
ele.get_attribute('')
ele.get_property('name') # 指定为只能获取name属性
ele.value_of_css_property('color') # 获取CSS的属性值，类似样式的验证

# 切换iframe
iframe=driver.find_element_by_id('iframeLoginIfm')
driver.switch_to.frame() # 切到iframe
driver.switch_to.parent_frame() # 切到上一层frame
driver.switch_to.default_content() # 切到最外面一层frame

# 切换浏览器窗口window
all_windows=driver.window_handles # 1、是获取打开的浏览器窗口总数
driver.switch_to.window(all_windows[-1]) # 2、切换浏览器窗口
driver.switch_to.window(all_windows[0]) # 3、切换到第一个浏览器窗口

# 切换到alert
alert=driver.switch_to.alert # 切换到alert
print(alert.text) # 输出alert内容
alert.accept() # 点击确定
alert.dismiss() # 点击取消
alert.send_keys() # 有文本的情况进行输入动作

# select下拉框，（3种方式）一定要是select标签的下拉框
Select(ele).select_by_index(1)
Select(ele).select_by_value("ask")
Select(ele).select_by_visible_text("问答")

# 等待
# 全局固定等待
driver.implicitly_wait(10)
# 条件等待


# 远程服务器运行(docker搭建远程服务)
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver=webdriver.Remote(
    command_executor="http://47.100.175.61:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)

# 手机模拟器操作
mobile_emulation={"deviceName":'Nexus 5'}
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('mobileEmulaton',mobile_emulation)



