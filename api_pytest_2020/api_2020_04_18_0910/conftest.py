import pytest
import requests
from api_2020_04_18_0910.api_10_01 import login,update_info,get_info


@pytest.fixture("session")
def login_fixture():
    print("输入密码现代呢路")
    s=requests.session()
    login(s)
    # return s
    yield s
    print("后置操作")
    # s.close()


@pytest.fixture()
def unlogin_fixture():
    print("不登陆")
    s = requests.session()
    return  s