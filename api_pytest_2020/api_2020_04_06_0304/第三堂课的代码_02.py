import requests

import urllib3
urllib3.disable_warnings() # 忽略警告


url = "https://www.cnblogs.com/yoyoketang/?_wv=1031"

# verify=False https忽略证书校验
r = requests.get(url, verify=False)
print(r.text)   # 文本

