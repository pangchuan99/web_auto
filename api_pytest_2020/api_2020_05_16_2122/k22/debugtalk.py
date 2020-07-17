


import requests



host = "http://49.235.92.12:6009"



def get_token(user, psw):
    body = {
        "username": user,
        "password": psw
    }
    s = requests.session()
    r = s.post(host+"/api_2020_05_30_2930/v1/login", json=body)
    token = r.json()["token"]
    return token

if __name__ == '__main__':
    t = get_token("test","123456")
    print(t)