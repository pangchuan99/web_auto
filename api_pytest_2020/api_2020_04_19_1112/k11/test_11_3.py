from api_2020_04_18_0910.api_10_01 import update_info
import pytest
from api_2020_04_19_1112.k11.read_yaml import get_yaml_data
import os

# 获取当前文件的上一层路径
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
# 然后在获取某一个文件的绝对路径
yamlpath = os.path.join(curpath, "update_infoy.yml")
print(yamlpath)
testdata1= get_yaml_data(yamlpath)
print(testdata1)



@pytest.mark.skip    #跳过这条用例
def test_2():
    '''已经知道这个接口有BUG'''
    print("已经知道这个接口有BUG")



def test_3():
    '''已经知道这个接口有BUG333'''
    print("已经知道这个接口有BUG")

# test_datas= [
#                           ["F",{'message': 'update some data!', 'code':0}],
#                           ["M",{'message': 'update some data!', 'code':0}],
#                           ["X",{'message':'参数类型错误','code':3333}]
#                           ]

@pytest.mark.parametrize("test_input,exe",
                         testdata1["test_info_params"],
                         # ids=[
                         #     "修改个人信息sex=M，成功",
                         #     "修改个人信息sex=F，成功",
                         #     "修改个人信息sex=Y,异常场景",
                         # ]
)#ids注释文档
def test_info_9(login_fixture1,test_input,exe):
    '''测试修改个人信息接口'''

    s=login_fixture1
    print("用例1")
    # s=login(s)
    print(s.headers)
    # if not s.headers.get("Authorization"):
    #     pytest.skip("未登录成功，跳过后面的用例")
    #修改
    infos=update_info(s,name="test",sex1=test_input)
    # assert infos["data"]["mail"]=="13456@qq.com"
    assert infos["message"]== exe["message"]
    assert infos["code"] == exe["code"]
    print(infos)
    print(type(infos))



def test_369(login_fixture1):

    print("12345679")


@pytest.mark.xxx
def test_123(login_fixture1):
    print("张三")



@pytest.mark.xxx   #pytest -m xxx    pytest -m not xxx
def test_1234(login_fixture1):
    print("里斯")

