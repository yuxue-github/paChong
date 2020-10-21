from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import sys

def search(driver, keyword):
    print(keyword)
    driver.get("http://www.baidu.com")
    sleep(2)
    print("open baidu")
    elem = driver.find_element_by_name("wd")
    print(elem)
    elem.clear()  # 清空搜索框中的内容
    sleep(2)
    elem.send_keys(keyword)  # 在搜索框中输入
    elem.send_keys(Keys.RETURN)
    sleep(2)
    content = ''
    if "地址" in keyword:
        try:
            elem = driver.find_element_by_xpath('//*[@id="1"]/div/div[2]/div[3]/span[2]')
            if elem:
                content = elem.text
        except OSError:
            pass

    return content

def getContent(driver, item, key):
    content = search(driver, item + key)
    return key + ": " + content