

from selenium import webdriver

import pytest





driver=None
#声明他是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver  #global声明一个全局变量
    #前置操作
    print("=--------------类开始----------------")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    bp=Bidpage(driver)
    yield(driver,lg,bp) #这个关键字指的是分隔符  yield前面指的前置条件   yield后面是后置条件
                     #代表分割线：#后面接返回值
    #后置操作
    print("---------------结束----------------")
    driver.quit()
    pass

@pytest.fixture()
def refresh_page():
    global driver
    #前置操作
    yield
    driver.refresh()

    #后置操作



# @pytest.fixture(scope="session")
# def session_demon():
#     print("*************我是整个测试绘画期间的开始****************")
#     yield
#     print("**************我是整个测试绘画期间的结束***************")
#
