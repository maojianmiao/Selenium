#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2016

@author: maojianmiao
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from JDPages import *

def driver(url, remoteIP='local'):
    url = url
    if remoteIP != 'local':
        driver = webdriver.Remote('http://' + remoteIP + ':4444/wd/hub', DesiredCapabilities.FIREFOX)
    else:            
        driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.get(url)
    driver.maximize_window()
    return driver

def getStart():
    dr = driver('http://www.jd.com')
    #dr = driver('http://www.jd.com','172.16.46.183')
    return MainPage.MainPage(dr)
