import requests
import json

url = "http://49.235.92.12:6009/api/v1/loginhttp://49.235.92.12:9000/api/v1/login"



# Content-Type: application/json
body = {
    "username": "test3",
    "password": "123456"
}


h={
    "token":"123465798",
    "cookie":"456"
}

#有些参数是放到 headers 里面的  他比较特殊   ,有些需要用它来进行鉴权
#如果头部里面有cookie  那么就不用单独写出来了，头部没有那么就要写
c={
    "cookie": "ask风纪扣就"
}
r=requests.post(url,json=body,headers=h,cookies=c)
print(r.text)
print(json.dumps(r.json(),indent=4,ensure_ascii=False))







code=r.json()['code']
print("你获取到的code:{}".format(code))



msg=r.json()['msg']
print("你获取到的code:{}".format(msg))


username=r.json()['username']
print("你获取到的username:{}".format(username))


token=r.json()['token']
print("你获取到的Token:{}".format(token))
#断言是pytest 中的 assert    为真的情况下他是不会报错的   只有在两者不相等的情况下  才能报错
assert   msg=="login success!"