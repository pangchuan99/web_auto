import requests

s = requests.session()

# s.get()
# s.post()
# s.put()
# s.delete()

r1 = s.request(method="GET",
               url="",
               params={},
               headers={})
r2 = s.request(method="POST", url="", data="", json="")
print(r2.content)  # 返回byte类型
print(r2.headers)  # dict
print(r2.status_code)
