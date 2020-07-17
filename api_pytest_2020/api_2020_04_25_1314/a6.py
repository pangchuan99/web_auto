import requests
import json
import requests

def login(s, username="test", password="123456"):
    '''
    登陆
    :param s: requests.session()
    :param username: 账号
    :param password: 密码
    :return: s
    '''
    url = "http://49.235.92.12:6009/api/v1/login"
    body = {
        "username": username,
        "password": password
    }
    r = s.post(url, json=body)

    token = r.json()["token"]
    print(token)   # 获取到token
    # s.token = token
    h = {
            "Content-Type": "application/json",
            "Authorization": "Token %s"%token
        }
    s.headers.update(h)
    return s


class UserInfo():
    '''个人信息'''

    def __init__(self, s:requests.Session):
        self.s = s

    def update_info(self, name="test", mail="222@qq.com"):
        url = "http://49.235.92.12:6009/api/v1/userinfo"
        body = {"name": name,
                "sex": "M",
                "age": 23,
                "mail": mail}

        r = self.s.post(url, json=body)
        return r.json()

    def get_info(self):
        url = "http://49.235.92.12:6009/api/v1/userinfo"
        r = self.s.get(url)
        return r.json()

if __name__ == '__main__':
    s = requests.Session()
    # 先登陆
    login(s) # 函数

    info = UserInfo(s) # 实例化
    info.update_info()

    infos = info.get_info()
    print(infos)
