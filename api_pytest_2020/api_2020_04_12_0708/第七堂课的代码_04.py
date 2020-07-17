import requests
import json
url = "http://49.235.92.12:6009/api/v1/login"

body = {
	"username": "test",
	"password": "123456"
}



r = requests.post(url, json=body)

# print(r.text)  # json字符串
# requests  #requests库里面的内置的json解析器
a1=r.json()# 把json字符串转换成python的字典
print("我是啊",type(a1))
# print(r.json()["token"])


#没有解析器就要导入json 进行转换
json_dict = json.loads(r.text)   #json.loads()  json字符串转字典
print(type(json_dict))
print(json_dict)



#没有解析器就要导入json 进行转换

#json.dumps() 字典转json
json_json= json.dumps(r.json())
print(type(json_json))
print(json_json)


