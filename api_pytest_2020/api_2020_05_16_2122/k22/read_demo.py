import yaml
import os
# 读取出来
with open("test_login_info.yml","r",encoding="utf-8")as fp:
    t=fp.read()
    print(t)


b=yaml.load(t,Loader=yaml.FullLoader)
print(b)