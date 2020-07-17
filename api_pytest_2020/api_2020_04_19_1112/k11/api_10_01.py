import json
import requests





def login(s,username='test',pwd="123456"):
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": username,
        "password": pwd
    }
    r=s.post(url,body)
    token=r.json()["token"]
    #其他接口只需要获取就行了  他已经更新到头部
    h = {
                    "Content-Type": "application/json",
                    "Authorization": "Token {}".format(token)
                }
    s.headers.update(h)
    # print(s.headers)
    # print("登录之后显示：token:{}".format(token))
    return s

def update_info(s,name,mail,sex1):
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {"name": name,
            "sex": sex1,
            "age": 23,
            "mail": mail}
    r1=s.post(url,json=body)
    return r1.json()

def get_info(s):
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    r2=s.get(url)
    return r2.json()

if __name__ == '__main__':

    s = requests.session()
    # 登录
    login(s,"test","123456")
    # 修改
    infos=update_info(s)
    print(infos)
    #查询
    m=get_info(s)
    print(m)






#
#
#
#
#
#
#
#
#
# def login(s, username="test", password="123456"):
#     '''
#     登陆
#     :param s: requests.session()
#     :param username: 账号
#     :param password: 密码
#     :return: s
#     '''
#     url = "http://49.235.92.12:9000/api/v1/login"
#     body = {
#         "username": username,
#         "password": password
#     }
#     r = s.post(url, json=body)
#
#     token = r.json()["token"]
#     print(token)   # 获取到token
#     # s.token = token
#     h = {
#             "Content-Type": "application/json",
#             "Authorization": "Token %s"%token
#         }
#     s.headers.update(h)
#     return s
#
# def update_info(s, name="test", mail="222@qq.com"):
#     url = "http://49.235.92.12:9000/api/v1/userinfo"
#     body = {"name": name,
#             "sex": "M",
#             "age": 23,
#             "mail": mail}
#     r = s.post(url, json=body)
#     return r.json()
#
# def get_info(s):
#     url = "http://49.235.92.12:9000/api/v1/userinfo"
#     r = s.get(url)
#     return r.json()
#
#
# if __name__ == "__main__":
#     s = requests.session()
#     login(s)
#     infos = update_info(s, name="test", mail="xxx@qq.com")
#     print(infos)
#     # 查询
#     m = get_info(s)
#     print(m)
#
#





# url2 = "http://49.235.92.12:9000/api/v1/userinfo"
# h = {
#     "Content-Type": "application/json",
#     "Authorization": "Token %s"%token
# }
# r2 = requests.get(url2, headers=h )
# print(r2.text)
# print(r2.json())
# print(r2.json()['msg'])
# mail = r2.json()['data'][0]["mail"]
# assert mail == "283340479@qq.com"