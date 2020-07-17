
from api_2020_04_18_0910.api_10_01 import login,update_info,get_info
import requests

s = requests.session()
def test_get_info():

    # 登录
    s1=login(s)
    print(s1)
    # # 修改
    infos=update_info(s,name="test",mail="1487@qq.com",sex1="F")
    print(infos)
    # #查询
    m=get_info(s)
    print(m)


    # assert infos["data"]['mail'] == "xxx@qq.com"
    # assert m['data'][0]['mail'] == "xxx@qq.com"