
from selenium import webdriver
from PageObjects.login_page import LoginPage #元素定位页面

from PageObjects.index_page import IndexPage #首页页面
from TestDatas import Common_Datas  as CD    #地址
from TestDatas import login_datas   as  LD   #登录数据
from PageObjects.bid_page import Bidpage
import pytest

@pytest.mark.usefixtures("access_web")  # 在运行的时候，回去运行access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestInvest:

    # @pytest.mark.smoke
    def test_invest_1_success(self,access_web):
        access_web[1].login(LD.success_data["text"], LD.success_data["password"])
        access_web[2].invest()
        assert access_web[2].invest()=="监控员"
    # 断言

    def test_invest_2_failad_no100(self,access_web):
        # self.lg.login(LD.success_data["text"], LD.success_data["password"])
        access_web[2].get_uer_money()
    #     pass
    # def test_invest_failad_no10(self):
    #     pass
    #

