from api_2020_05_04_1516.K15.a1 import login_xadmin
import requests
from api_2020_05_04_1516.K15.connet_mysql import select_sql, execute_sql
from api_2020_05_04_1516.K15.a2 import add_01,add_tupian_wenjian
import pytest


# 前置操作：先清空数据
@pytest.fixture(scope="function")
def delete_teacher():
    sql = "DELETE FROM djangoweb.hello_teacher WHERE teacher_name = 'pc122'"
    execute_sql(sql)
    yield
    print("数据清理的操作")


#这个是用数据库进行清理
def test_add011(login_fixture1,delete_teacher):
    #登录
    s=login_fixture1
    #添加的数据
    add_01(s)
    sql = "SELECT count(*) as sum from djangoweb.hello_teacher WHERE teacher_name = 'pc122'"
    result1 = select_sql(sql)[0]['sum']
    # 添加之后查询
    # print("添加之后查询2：%s" % result1)
    # 去校验添加的结果
    assert result1 == 1

def test_add_tupain_wenjian(login_fixture1):
    #图片上传和文件上传
    #登录
    s=login_fixture1
    add_tupian_wenjian(s)

