import re
import os
from paChong import getContent
from selenium import webdriver

keyWords = ["地址"]

def readConfig():
    configList = []
    fp = open("config.txt", "r", encoding="utf-8")
    lines = fp.readlines()
    for line in lines:
        configList.append(line.strip('\n'))
    fp.close()
    return configList

def initBrowser():
    chromDriver = 'E:/yuxue/workspace/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromDriver)
    return driver

if __name__ == "__main__":
    configList = readConfig()
    output = open('result.txt', 'w', encoding='utf-8')
    driver = initBrowser()
    for item in configList:
        print(item)
        result = item + '\n'
        for key in keyWords:
            content = getContent(driver, item, key)
            result = result + content + '\n'
        output.write(result + '\n')
    output.close()
    driver.close()