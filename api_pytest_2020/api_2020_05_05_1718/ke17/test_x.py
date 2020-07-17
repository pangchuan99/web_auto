import allure


@allure.severity("critical")
@allure.feature("模块3：xxxxxx")
def test_01():
    '''用例1的描述：xxxx'''
    print("测试用例1")
    assert 2==2


@allure.severity("blocker")
@allure.feature("另一个文件的：模块名称18：xxxxxx")
@allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
def test_02():
    '''用例2的描述：22222222'''
    print("测试用例2")
    assert 2==2
