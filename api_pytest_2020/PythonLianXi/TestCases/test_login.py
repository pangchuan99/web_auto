import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage #元素定位页面
from PageObjects.index_page import IndexPage #首页页面
from TestDatas import Common_Datas  as CD    #地址
from TestDatas import login_datas   as  LD   #登录数据
import  ddt
import pytest

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #一个测试类只打开一次浏览器
        #通过excel读取本功能当中需要的所有测试数据
        print("=--------------类开始----------------")
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg = LoginPage(cls.driver)
        # cls.driver.save_screenshot()

    @classmethod
    def tearDownClass(cls):
        print("------类结束-------")

        cls.driver.quit()
        pass


    # #前置
    # def setUp(self):
    #
    #     pass


    #后置步骤

    def tearDown(self):
        self.driver.refresh()



    #正常用列---登录成功
    @pytest.mark.smoke
    @ddt.data(*LD.phone_data)
    def test_login_1_wrongPwd_noReg(self,data):
        # 前置 访问登录页面
        # 步骤 输入用户名 密码 点击登录
        self.lg.login(data["text"], data["password"])
        # 断言  登录页面内  提示：用户密码错误！
        self.assertEqual(self.lg.get_errorMsg_from_pageCenter(),data["check"])

    @pytest.mark.smoke
    def test_login_2_success(self):
        #前置 访问登录页面
        #步骤 输入用户名 密码 点击登录
        self.lg.login(LD.success_data["text"],LD.success_data["password"])
        #断言
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

        #等待时间
        #找元素



    # #这种是页面提示错误
    # @ddt.data(*LD.phone_data)
    # #异常用列---手机格式不正确(大于11位，小于11位，为空，不在号码段)
    # def test_logon_user_wrongFormt(self,data):
    #
    #     # 前置 访问登录页面
    #     # 步骤 输入用户名 密码 点击登录
    #     self.lg.login(data["user"], data["password"])
    #     # 断言  登录页面内  提示：请输入正确的手机号
    #     #登录页面中---获取提示框的文本内容
    #     #比对文件内容与期望的值 是否相等
    #     self.assertEqual(self.lg.get_erroMsg_from_loginArea(),data[""])
    #

    #这种是弹出框提示错误
     #异常用列---用户名为空


    #异常用列---未注册手机号
    #异常用列---错误的密码




#pageobjeects去调用-------pagelocators
#testcases=pageobjects+testdatas
#都是单向调用