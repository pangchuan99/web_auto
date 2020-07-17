from api_2020_04_18_0910.api_10_01 import login,update_info,get_info

def test_info_1(login_fixture):
    print("用例1")
    s=login_fixture
    print(s.headers)
    #修改
    infos=update_info(s,name="test",mail="13456@qq.com",sex1="F")
    assert infos["data"]["mail"]=="13456@qq.com"
    print(infos)
