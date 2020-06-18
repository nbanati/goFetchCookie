# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
 
def goFetchCookie():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(loginUrl)
    driver.find_element_by_xpath("accept_cookie_banner_close__button_xpath").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("email").click()
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").click()
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("submitBtn").click()
    cookies=driver.get_cookies()
    c=""
    for cookie in cookies:
        if cookie['name']==cookiename:
            c=cookie['value']
    f=open(outputFile, "a+")
    f.write(str(datetime.now())+"\t"+c+"\n")

loginUrl="xxx"
username="xxx"
password="xxx"
cookiename="xxx"
outputFile="C:\\path\\cookies.txt"
goFetchCookie()