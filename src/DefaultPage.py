#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 17, 2016

@author: maojianmiao
'''

from selenium.webdriver.common.by import By
from PageBase import PageBase
import TestBase

'''
    Page Elements
'''
discover = (By.LINK_TEXT,'Discover')
assets = (By.LINK_TEXT,'Assets...')
manage = (By.LINK_TEXT,'Manage')
endpoint = (By.LINK_TEXT,'Endpoints')
wakenow = (By.LINK_TEXT,'Wake Now...')
export = (By.LINK_TEXT,'Export')
titleBox = (By.XPATH,'//div/input[contains(@id,"JobNameTextBox")]')
nextBut = (By.XPATH,'//div/input[contains(@id,"NextButtonView")]')
ok = (By.LINK_TEXT,'OK')

class jsPage(PageBase):
    def __init__(self,driver):
        self.driver = driver
    
    def setAssetTitle(self, title):
        self.sendkeys(titleBox, title)
        return jsPage(self.driver)
    
    def ClickNext(self):
        self.click(nextBut)
        return jsPage(self.driver)
    
    def checkWindowsAlert(self):
        win = self.getCurrentWindow()
        self.click(ok)
        self.driver.switch_to.windows(win)
        return jsPage(self.driver)
    
class defaultPage(PageBase):
    def __init__(self,driver):
        self.driver = driver
    
    def Manage_Endpoints(self):
        self.mouseToElement(manage)
        self.click(endpoint)
        return defaultPage(self.driver)
    
    def ExportFiles(self):
        self.click(export)
        return defaultPage(self.driver)
    
    def Discover_Assets(self):
        self.mouseToElement(discover)
        self.click(assets)
        self.toNewWindow()
        return jsPage(self.driver)
        

dr = TestBase.GetStart('https://172.16.146.119','172.16.46.183')
de = defaultPage(dr)
de.Discover_Assets().setAssetTitle('test').ClickNext()
print de.getCurrentWindow()

        