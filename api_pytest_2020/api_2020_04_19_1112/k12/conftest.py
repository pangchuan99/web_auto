import pytest

import requests



@pytest.fixture(scope="session")
def unlogin_333():
    '''不登陆的'''
    s=requests.session()
    print("不登录")
    # return s
    yield s
    print("后置需要处理的操作")