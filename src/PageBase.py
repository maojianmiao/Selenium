#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2016

@author: maojianmiao
'''

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

class PageBase(object):
    #driver = webdriver.Remote()
    windowsHandlesBefore = []
    preWindow = ''
    
    def __init__(self, driver):
        self.driver = driver
        
    def sendkeys(self, byw, value): 
        elem = self.driver.find_element(*byw)
        elem.clear()
        elem.send_keys(value)
        
    def getWindowsHandle(self):
        retry = 3
        while retry>0:
            try:
                return self.driver.window_handles
                break
            except Exception,e:
                retry-=1
                time.sleep(0.5)
                print(e)
        
    #鼠标移动至某元素，可以显示javascrpt做成的动态页面
    def mouseToElement(self,byw):
        self.action = ActionChains(self.driver)
        elem = self.driver.find_element(*byw)
        self.action.move_to_element(elem).perform()
        time.sleep(1)
        
    def selectDorpList(self, byw, value):
        select = Select(self.driver.find_element(*byw))
        select.select_by_value(value) 
         
    #单击元素   
    def click(self,byw):
        self.windowsHandlesBefore = self.getWindowsHandle()
        self.driver.find_element(*byw).click()
        
     
    def getCurrentWindow(self):
        return self.driver.execute_script('return window.name')
    
    def toNewWindow(self):
        self.preWindows = self.getCurrentWindow()
        self.windowsHandlesAfter = self.getWindowsHandle()
        try:
            for win in self.windowsHandlesAfter:
                if win not in self.windowsHandlesBefore: 
                    self.driver.switch_to_window(win)
        except Exception,e:
            logging.error("Can't navaite to new windows, please check")
            
    def toPreWindow(self):
        self.driver.switch_to_window(self.preWindow)
    ##
    def checkAlert(self,confirm):
        try:
            alert = self.driver.switch_to().alert()
        except Exception,e:
            logging.exception('Failed to switch to alert %s',e)
        
        if confirm:
            alert.accept()
        else:
            alert.dismiss()
        logging.info('Alert on Page: %s | %s.',self.driver.current_url(), alert.text())
            
    def dispose(self):
        self.driver.close()
    
    def getScreenShot(self):
        if not os.path.exists(r'c:\autoPic'):
            os.makedirs(r'c:\autoPic')
        file = 'c:\\autoPic\\' + time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) + '.png'
        self.driver.get_screenshot_as_file(file)
        logging.info('File is stored')
        
    def getTitle(self):
        return self.driver.title
    
    def getSource(self):
        return self.driver.page_source
    
    def isSelect(self,byw):
        elem = self.driver.find_element(*byw)
        return elem.is_selected()
    
    def isDisplayed(self,byw):
        elem = self.driver.find_element(*byw)
        logging.info(elem)
        return elem.is_displayed()
    
    def getText(self,byw):
        elem = self.driver.find_element(*byw)
        return elem.text
    
    def refresh(self):
        self.driver.refresh()