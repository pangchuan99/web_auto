
a = None
print(type(a))   # type函数，查看数据类型 <class 'NoneType'>
u = ""
print(type(u))  # str


b = 123
print(type(b))  # int
c = 1.02
print((type(c)))  # float
d = "hello world!"
print(type(d))  # str
e = "123"       # str
print(type(e))
f = 'hello' \
    'world'
print(f)
g = '''hello
world
多行
'''
print(type(g))
print(g)

# list
h = [1, 1, 2, 3, None, "hello"]  # list
print(type(h))
print(h.append("world"))
print(h)
# tuple  元组类型
j = (1, 2, 3, None, "hello")
print(type(j))
print()

# dict

m = {
    "username": "admin",
    "passworld": "123456",
    "user": "admin",
    1: "2222222",
    122.2: "cccccc",
    "a": None,
    "b": 1233,
    "c": [1, 3, 4, 5],
    "d": (1, 2, 4),
    "e": {
        "aaaa": "111111",
        "bbbb": "111111",
    }
}
# key:value
print(type(m))  # <class 'dict'>
print(m)

m["username"] = "new admin"  # 改变key对应的值
print(m)
m["new"] = "new value"  # 新增
print(m)
print(m["username"])  # 查询

del m["username"]  # 删除
print(m)

print(m["e"]["aaaa"])


y = True
t = False   # bool