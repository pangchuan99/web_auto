import allure


@allure.step("登录")
def login():
    '''登录操作'''


@allure.step("进行增")
def add_xx():
    pass


@allure.description("测试描述")
@allure.step("进行修改")
def modify_aaa():
    '''修改aaa内容'''

@allure.step("进行删除操作")
def get_xxx():
    '''查询xxx内容'''
    pass
