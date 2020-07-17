#token    对外接口开发，纯接口，前后端分离
#cookies  用于网站开发
import urllib3
urllib3.disable_warnings()  # 忽略警告


import requests

# s = requests.Session()  # Session的实例
# #
# # print(s.headers)
# #
# # h = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# # }
# # s.headers.update(h)
# # print(s.headers)  # 伪装成浏览器User-Agent
# # r1 = s.get("https://www.baidu.com/", verify=False)
# # print(s.verify)
# # s.verify = False
# #
# # print(s.verify)
#
# # r2 = s.get("https://www.baidu.com/")
# # print(r2.text)





r=requests.session()  #session  与Session 一样

print(r.headers)

h={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'

}
r.headers.update(h)
print(r.headers)   #伪装成浏览器



r=requests.session()  #session  与Session 一样

# 访问HTTPS  证书问题  他默认是verify=True
# print(r.verify)
# r.verify=False
# print(r.verify)
r1=r.get("https://www.baidu.com/")
print(r1.text)






