import json

d = {
    "a": None,
    "b": 1222,
    "c": "hello",
    "d": True,
    "e": [1, 2, 3, True, None, "hello", False],
    "g": (1,3,4),
    "f": {
        "username": "中文",
        "password": "123456"
    }
}

#字典打印出来是---单音符输出
print(type(d))
print(d)




#字典转JSON     json.dumps()
d_json=json.dumps(d)
# d_json=json.dumps(d,indent=4,ensure_ascii=False)  #他只适用于字典转JSON   indent=4,ensure_ascii=False
print(type(d_json))
print(d_json)
print(type(d_json))


#json转字典
d_dict=json.loads(d_json)
print(type(d_dict))
print(d_dict)













# print(d)
# print(type(d))
# # 标注输出
# # {'a': None, 'b': 1222, 'c': 'hello', 'd': True, 'e': [1, 2, 3, True, None, 'hello', False], 'f': {'username': 'aaaaa', 'password': '123456'}}
#
#
# # 转json ensure_ascii=False
# d_json = json.dumps(d, indent=4, ensure_ascii=False)
# print(d_json)
# print(type(d_json))
# # {"a": null, "b": 1222, "c": "hello", "d": true, "e": [1, 2, 3, true, null, "hello", false], "f": {"username": "aaaaa", "password": "123456"}}
#
# f = '{"a": null, "b": 1222}'
# g = {"a": None, "b": 1222}
#
# # 转字典
# json_dict = json.loads(d_json)
# print(json_dict)