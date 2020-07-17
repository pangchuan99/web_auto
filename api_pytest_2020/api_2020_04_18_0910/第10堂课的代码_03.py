# from ke10.common_fuctions import login, update_info, get_info
import requests
from api_2020_04_18_0910.api_10_01 import login,update_info,get_info


s = requests.session()

def setup_module():
    '''前置操作，整个模块开始用例前只执行一次'''
    login(s)    # 1.登陆
    print('前置操作，整个模块开始用例前只执行一次')


def teardown_module():
    print('后置操作，整个模块开始用例前只执行一次')


def setup_function():
    print("每个测试用例之前，都会执行一次")

def teardown_function():
    print("每个测试用例后置操作，都会执行一次")

def test_get_info():
    '''成功'''
    infos = update_info(s, name="test", mail="1234@qq.com")
    print(infos)  # 2.修改

    assert infos["data"]['mail'] == "1234@qq.com"


def test_get_info_1():
    '''修改其他人的个人信息'''
    # s = requests.session()
    # login(s)    # 1.登陆
    infos = update_info(s, name="test1", mail="xxx@qq.com")
    print(infos)  # 2.修改

    assert infos['message'] == '无权限操作'

