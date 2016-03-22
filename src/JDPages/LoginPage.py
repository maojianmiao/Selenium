#!c:\Python27\python.exe
#coding:utf-8
'''
Created on Mar 21, 2016

@author: maojianmiao
'''
from selenium.webdriver.common.by import By
from PageBase import PageBase
import TestBase
import MainPage
import logging
import unittest

class LoginElement(object):
    username = (By.XPATH,'//div/input[@id="loginname"]')
    passwd = (By.XPATH,'//div/input[@id="nloginpwd"]')
    autoLogin = (By.XPATH,'//div/span/input[@id="autoLogin"]')
    autoLoginMsg = (By.XPATH,'//div[contains(@class,"msg-warn")]')
    loginSumbit = (By.XPATH,'//div/a[@id="loginsubmit"]')
    loginAlert = (By.XPATH,'//div[contains(@class, "msg-error")]')
    
class LoginPage(PageBase):
    
    title = '京东-欢迎登录'
    
    def __init__(self,driver):
        self.driver = driver
        
    def loginWith(self,username=None,passwd=None):
        if username:
            self.sendkeys(LoginElement.username, username)
        if passwd:
            self.sendkeys(LoginElement.passwd, passwd)
        return LoginPage(self.driver)
    
    def clickSubmit(self):
        self.click(LoginElement.loginSumbit)
        if self.getTitle() == self.title:
            return self
        else:
            return MainPage.MainPage(self.driver)
    
    def isAutoLoginSelect(self):
        return self.isSelect(LoginElement.autoLogin)
    
    def assertErrorDisplayed(self):
        try:
            assert self.isDisplayed(LoginElement.loginAlert) is True
            logging.info('login error is displayed, error message is: %s', self.getText(LoginElement.loginAlert))
        except Exception,e:
            logging.error('login error is not displayed\n%s',e)
            raise AssertionError
        
    def getLoginMessage(self):
        if self.isDisplayed(LoginElement.loginAlert):
            return self.getText(LoginElement.loginAlert)
        elif self.isSelect(LoginElement.autoLogin):
            return self.getText(LoginElement.autoLoginMsg)
        else:
            logging.info('No Mssage displayed')
            return None