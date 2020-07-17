import requests
import json


url= "http://apis.juhe.cn/simpleWeather/query"

body={
    "key": "5a731258401fc3af244873d094ac6564",
    "city": "成都"
}

r=requests.get(url,params=body)
# print(r.text)
print(json.dumps(r.json(),indent=4,ensure_ascii=False))#他只适用于字典转JSON   indent=4,ensure_ascii=False

print(json.loads(r.text))

#indent=4 是json格式那么就可以 空格4
#ensure_ascii=False  出现乱码就可以使用


