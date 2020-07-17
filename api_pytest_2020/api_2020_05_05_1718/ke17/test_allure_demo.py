import pytest
from api_2020_05_05_1718.ke17.common_function import add_xx,modify_aaa,get_xxx,login
import allure












@allure.feature("模块1：test_01")
@allure.story("进行登录")    #自己加一个目录标题
@allure.description("他是用来描述的")
def test_01():
    login()
    '''用例1的描述：xxxx'''
    print("测试用例1")



@allure.feature("模块2 test_02")
@allure.title("标题2")
@allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
def test_02():
    '''用例2的描述：22222222'''
    print("测试用例2")





@allure.feature("模块名称test_03---执行添加老师和上传图片和文件")
@allure.title("具体某一个测试用例title是标题---test_03")
@allure.story("story用例的标题：修改个人信息-sex参数为空")
@allure.description("具体来描述这个用例是干嘛的")
@allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-366-1.html")
def test_03(login_fixture):
    # '''用例3的描述：3333'''
    # print("测试步骤1：")
    add_xx()
    # print("测试步骤2：")
    modify_aaa()
    # print("测试步骤3：查询")
    get_xxx()


@allure.description("他是来站位置的 ")
def test_04():
    pass

