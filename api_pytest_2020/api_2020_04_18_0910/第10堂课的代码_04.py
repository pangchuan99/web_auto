from api_2020_04_18_0910.api_10_01 import login,update_info,get_info
import requests


class TestInfo():

    def setup_class(self):
        '''前置操作，整个class开始用例前只执行一次'''
        print('前置操作class，整个class开始用例前只执行一次')

    def teardown_class(self):
        print('后置操作class，整个class开始用例前只执行一次')

    def setup_method(self):
        '''前置操作，整个class开始用例前只执行一次'''
        print('前置操作method，整个method开始用例前只执行一次')

    def teardown_method(self):
        print('后置操作method，整个method开始用例前只执行一次')

    def test_get_info_1(self):
        '''成功'''
        print("用例1")

    def test_get_info_2(self):
        '''修改其他人的个人信息'''
        print("用例2")

    def test_get_info_3(self):
        '''修改其他人的个人信息'''
        print("用例2")
        