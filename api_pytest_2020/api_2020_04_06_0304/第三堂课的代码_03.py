import requests
import json


url= "http://apis.juhe.cn/simpleWeather/query"

body={
    "key": "5a731258401fc3af244873d094ac6564",
    "city": "成都"
}

r=requests.get(url,params=body)


#返回的结果
print(r.text)   #str
print(type(r.text))

print(r.json())
print(type(r.json()))# 字典

print(r.status_code) #返回状态码
print(r.headers)     #返回头部   类型是字典
print(r.headers['Content-Type'])  #取返回头部中的某一个

print(r.cookies)  # RequestsCookieJar类型
print(dict(r.cookies))   #转换成字典类型的
print(r.cookies['aliyungf_tc'])  #取他某一个值

print(r.encoding)#编码---utf-8
print(r.url)  #这个是访问最终的地址    有些网址是重定向

print(r.content.decode("utf-8")) #byte类型  当text出现乱码的时候 就用这个(万能)


print(json.dumps(r.json(),indent=4,ensure_ascii=False))
