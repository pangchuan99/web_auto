import requests
#使用正则表达式
import  re

url = "http://49.235.92.12:8020/admin/login/?next=/admin/ "
#session
s=requests.session()
r=s.get(url)
# print(r.text)
#input type='hidden' name='csrfmiddlewaretoken' value='JGPvzectwpvkbSgUze5GtHT9X3tdZxU0vtbBy47gG2d2QcMUZZIr6TgX34p7dA5W' />

            #查找 进行配置规则
csrf_token=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
print(csrf_token[0])
h={
    "cookie":"1"
}
body={
    "csrfmiddlewaretoken":csrf_token[0],
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/"
}
#主要是 前端  form  表单里面 type="hidden"他是隐藏参数，需要在前端进行获取（#使用正则表达式）
r1=s.post(url,data=body)


print(r1.text)

# print(r1.headers["Connection"])
# print(r1.headers["Cookie"])