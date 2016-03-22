#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2016

@author: maojianmiao
'''
from selenium.webdriver.common.by import By
from PageBase import PageBase
import TestBase
import LoginPage

class MainElement(object):
    
    pageURL = 'http://www.jd.com'
    title = '京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！'
    #送至：。。。
    takeTo = (By.XPATH,'//*[@id="ttbar-mycity"]/div[contains(@class,"areamini")]')
    #网站导航
    siteMap = (By.XPATH,'//*[@id="ttbar-navs"]/div/i')
    #登录连接
    loginLink = (By.XPATH,'//ul/li/a[@class="link-login"]')

    
class MainPage(PageBase):
    def __init__(self, driver):
        self.driver = driver
        
    def takeTo(self): 
        self.mouseToElement(MainElement.takeTo)
        return MainPage(self.driver)
    
    def siteMap(self): 
        self.mouseToElement(MainElement.siteMap)
        return MainPage(self.driver)
    
    def clickLogin(self):
        self.click(MainElement.loginLink)
        return LoginPage.LoginPage(self.driver)
        