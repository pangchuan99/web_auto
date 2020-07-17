from api_2020_04_19_1112.k12.common_fuction import  register
from api_2020_04_19_1112.k12.connet_mysql import execute_sql
import pytest




#在这里编写前置的意思是要用到这个就去调用它
@pytest.fixture(scope="function")
def delete_register_1():
    print('前面的操作')
    '''执行sql，删除注册'''
    sql='DELETE FROM auth_user WHERE username="test333999"'
    execute_sql(sql)
    yield
    print("后面的操作")



#调用这个删除语句   他是先执行的
def test_register_1(delete_register_1,unlogin_333):
    s = unlogin_333
    r = register(s)
    print(r.json())
    assert r.json()['msg'] == '注册成功!'
    assert r.json()['code'] == 0



def test_register_2(unlogin_333,delete_register_1):
    '''测试用例，用户已注册'''
    s=unlogin_333
    r=register(s)#注册
    print(r.json())
    r3 = register(s) #重复注册
    print(r3.json())
    assert r.json()['msg']=='注册成功!'
    assert r.json()['code']==0
    assert '用户已被注册'in r3.json()['msg']
    assert r3.json()['code'] == 2000

