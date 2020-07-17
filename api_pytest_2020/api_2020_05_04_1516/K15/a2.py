from api_2020_05_04_1516.K15.a1 import login_xadmin
import requests
import re
from requests_toolbelt import MultipartEncoder
from api_2020_05_04_1516.K15.connet_mysql import select_sql
import os
from api_2020_05_04_1516.K15.c import host
# host=os.environ["host"]

def add_01(s):
    # 添加老师页面
    url = host+"/xadmin/hello/teacherman/add/"
    r=s.get(url)
    #查看隐藏参数然后进行正则匹配
    # print(r.text)
    csrftoken=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
    print(csrftoken[0])
    print(csrftoken[1])


    #其实可以用字典的但是  key值必须是唯一  他这里有两个所以不能用字典
    body=MultipartEncoder(fields=  [
        ("csrfmiddlewaretoken", csrftoken[0]),
        ("csrfmiddlewaretoken", csrftoken[0]),
        ("teacher_name", "pc122"),
        ("tel", "122222222"),
        ("mail", "1111@qq.com"),
        ("sex", "M"),
        ("_save", "")
    ])
    #需要添加头部参数headers={"content-type":body.content_type}
    r2=s.post(url,data=body,headers={"content-Type":body.content_type})
    # print(r2.text)




def add_tupian_wenjian(s):
    url3 =host+"/xadmin/hello/fileimage/add/"
    r = s.get(url3)
    # print(r.text)

    csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
    # print(csrftoken)
    body3 = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken", csrftoken[0]),
            ("csrfmiddlewaretoken", csrftoken[0]),
            ("title", "pc上传图片测试88888"),
            #上传图片
            ("image", ("122.png", open("122.png", "rb"), "image/png")),
            #上传文件
            ("fiels", ("122.png", open("122.png", "rb"), "image/png")),
            ("_save", "")

        ]
    )
    r3= s.post(url3, data=body3,headers={"content-Type": body3.content_type})
    # print(r3.text)



# 这个是  不清理处理进行断言数据  添加后减去添加前的
if __name__ == '__main__':
    s = requests.session()
    login_xadmin(s)

    sql = "SELECT count(*) as sum from djangoweb.hello_teacher WHERE teacher_name = 'pc122'"
    result1=select_sql(sql)[0]['sum']
    #添加之前查询
    print("添加之前查询1：%s" % result1)
    add_01(s)
    result2=select_sql(sql)[0]['sum']
    #添加之后查询
    print("添加之后查询2：%s" %result2)

    #添加之后减去添加之前的
    assert result2-result1==1

    # #验证上传图片和上传文件
    add_tupian_wenjian(s)
