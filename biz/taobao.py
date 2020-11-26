# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'ad771d7a',
    'noReset': True,
    'platformVersion': '10',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.welcome.Welcome',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
    'resetKeyboard': True  # 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
sleep(10)
# driver.wait_activity("com.taobao.tao.TBMainActivity", 5)

driver.find_element_by_name('搜索')
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# sleep(5)
# driver.find_element_by_id('com.taobao.taobao:id/searchEdit').click()
sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"hao")
sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
sleep(5)
