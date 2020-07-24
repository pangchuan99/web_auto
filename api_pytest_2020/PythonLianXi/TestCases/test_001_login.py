import pytest
from selenium import webdriver




@pytest.mark.usefixtures("access_web")#在运行的时候，回去运行access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    @pytest.mark.parametrize("data",LD.phone_data)
    def test_login_1_wrongPwd_noReg(self,access_web,data):
        # 前置 访问登录页面
        # 步骤 输入用户名 密码 点击登录
        access_web[1].login(data["text"], data["password"])

        # 断言  登录页面内  提示：用户密码错误！
        assert access_web[1].get_errorMsg_from_pageCenter()==data["check"]
    #
    #正常用列---登录成功    #fixture的函数名称，用来接收他的返回值
    @pytest.mark.parametrize("data",LD.success_data)
    def test_login_2_success(self,access_web,data): #finxture的函数名称作为用例函数，用力啊接收fixture的返回
        assert IndexPage(access_web[0]).isExist_logout_ele()

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