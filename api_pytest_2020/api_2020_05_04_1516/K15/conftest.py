import  pytest
import requests
from api_2020_05_04_1516.K15.a1 import login_xadmin
import os
# request  是pytest 内置的fixture

@pytest.fixture(scope="session")
def login_fixture1(request):
    '''登录 前置操作'''
    s=requests.session()
    login_xadmin(s)
    yield s
    print("后置操作")
    s.close()


    # #先执行前置 在执行后置
    # def close_s():
    #     s.close()
    #     def close_x():
    #         print("关闭其他的线程")
    #     request.addfinalizer(close_s)
    #     request.addfinalizer(close_x)
    #     return s
    # 添加命令行参数  parser内置fixture
# def pytest_addoption(parser):
#     parser.addoption("--cmdhost",action="stroe",
#                      default="http://49.235.92.12:8020",
#                      help=" my option:host1 or host2"
#                      )
#
# @pytest.fixture(scope="session",autouse=True)
# def host(request):
#     '''设置环境变量'''
#     os.environ["host"] =request.config.getoption("--cmdhost")
#



# # 添加命令行参数  parser内置fixture
# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdhost", action="store",
#         default="http://49.235.92.12:8020",
#         help="my option: host1 or host2"
#     )
#
# @pytest.fixture(scope="session", autouse=True)
# def host(request):
#     '''设置环境变量，自动生效'''
#     os.environ["host"] = request.config.getoption("--cmdhost")
#

