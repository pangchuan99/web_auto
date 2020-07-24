
from selenium import webdriver

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

