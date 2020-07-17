import yaml
import os
# 读取出来
with open("demo.yaml","r",encoding="utf-8")as fp:
    t=fp.read()
    # print(t)




#读出来的字段从，转成dict(字典)
a=yaml.load(t,Loader=yaml.FullLoader)
print(a)#打印出来是{'username': 'admin', 'password': 123456}  123456是整数没有把他当成字符串  需要在yaml格式里进行添加单引号'123456'





#读取出来另一个文件的,注意文件里面格式需要空格一下
with open("demo_list.yaml","r",encoding="utf-8")as fp:
    x=fp.read()
    # print(t1)

b=yaml.load(x,Loader=yaml.FullLoader)
print(b)




#读取出来另一个文件的,注意文件里面格式需要空格一下
with open("demo_list1.yaml","r",encoding="utf-8")as fp:
    x1=fp.read()
    # print(t1)

b1=yaml.load(x1,Loader=yaml.FullLoader)
print(b1)



curpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(curpath)
# # 然后在获取某一个文件的绝对路径
yamlpath = os.path.join(curpath, "api_2020_05_05_1718", "test_userinfo111.yaml")
print(yamlpath)

#读取出来另一个文件的,注意文件里面格式需要空格一下
fp =open(yamlpath, "r", encoding="utf-8")
x11=fp.read()
print(x11)

b11=yaml.load(x11,Loader=yaml.FullLoader)
print(b11)