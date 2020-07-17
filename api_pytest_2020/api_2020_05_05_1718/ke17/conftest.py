import pytest
import allure

@pytest.fixture(scope="session")
@allure.feature("名称")
@allure.description("前置登录操作123456798")
@allure.story("123")
@allure.title("456")
@allure.step("zhangsjdak jfsjfks jfksjfksjfklajfklsj")
def login_fixture():
    pass

    print("前置操作:登录")




# @allure.feature(是模块名称)
# # # # # # @allure.story(标题)
# # # # # # @allure.title(重命名用例标题)
# # # # # # @allure.description(描述)
# # # # # # @allure.step(操作步骤)