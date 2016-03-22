#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 21, 2016

@author: maojianmiao
'''
from selenium.webdriver.common.by import By
from PageBase import PageBase
from TestBase import getStart
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.flow = getStart()
        self.page = self.flow.clickLogin()
        self.title = self.page.getTitle()
        
    def test_verifyAutoLoginCheckMsg(self):
        self.assertTrue(self.page.isAutoLoginSelect(), '已选择自动登录 ')
        self.assertIn('公共场所不建议自动登录，以防账号丢失', self.page.getLoginMessage(), '提示信息：' + self.page.getLoginMessage())
        self.page.dispose()
        
    def test_noInputAndSubmit(self):
        afterLoginPage = self.page.loginWith().clickSubmit()
        self.assertEquals(afterLoginPage.getTitle(), self.title)
        self.assertIn('请输入账户名和密码', afterLoginPage.getLoginMessage(), '提示信息： ' + afterLoginPage.getLoginMessage())
        print afterLoginPage.getLoginMessage()
        self.page.dispose()
        
    @unittest.skip('this test would be failed because of code issue or by designed')
    def test_noPasswdAndSubmit(self):
        afterLoginPage = self.page.loginWith(username='fakeacount').clickSubmit()
        self.assertEquals(afterLoginPage.getTitle(), self.title)
        self.assertIn('请输入密码', afterLoginPage.getLoginMessage(), '提示信息： ' + afterLoginPage.getLoginMessage())
        print afterLoginPage.getLoginMessage()
        self.page.dispose()
        
    def test_noAcountAndSubmit(self):
        afterLoginPage = self.page.loginWith(passwd='fakepasswd').clickSubmit()
        self.assertEquals(afterLoginPage.getTitle(), self.title)
        self.assertIn('请输入账户名', afterLoginPage.getLoginMessage(), '提示信息： ' + afterLoginPage.getLoginMessage())
        print afterLoginPage.getLoginMessage()
        self.page.dispose()
        
    def test_errorInfoLogin(self):
        afterLoginPage = self.page.loginWith('fakeacount','fakepasswd').clickSubmit()
        self.assertEquals(afterLoginPage.getTitle(), self.title)
        self.assertIn('账户名不存在，请重新输入', afterLoginPage.getLoginMessage())
        self.page.dispose()
    
    @unittest.skip('No account for this test')
    def test_rightInfoLogin(self):
        afterLoginPage = self.page.loginWith('rightacount','rightpasswd').clickSubmit()
        self.assertEquals(afterLoginPage.getTitle(), '京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！')
        self.page.dispose()
'''        
if __name__ == "__main__":
    unittest.main()
''' 
suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
unittest.TextTestRunner(verbosity=2).run(suite)
