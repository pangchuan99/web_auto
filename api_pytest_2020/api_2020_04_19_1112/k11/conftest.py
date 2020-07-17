import pytest
import requests
from api_2020_04_18_0910.api_10_01 import login,update_info,get_info


@pytest.fixture()
def login_fixture1():
    '''先登录'''
    print("请先输入密码")
    s=requests.session()
    login(s)
    if not s.headers.get("Authorization"):
        pytest.skip("未登录成功，跳过后面的用例")
    # return s
    yield s
    print("后置操作结束")
    # s.close()


@pytest.fixture()
def unlogin_fixture():
    '''不登录'''
    print("不登陆")
    s = requests.session()
    return  s