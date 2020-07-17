import json
b = '{"a": True, "b": "bbb"}'
d = '{"a": true, "b": "bbb"}'
e = "{'a': True, 'b': 'bbb'}"

# print(eval(b))
# print(eval(e))

# json.dumps()
# json.loads()
#
# json.dump()
# json.load()


with open("aaa.txt", "r", encoding="utf-8") as fp:
	b = json.load(fp)
	print(b)


	 # a = fp.read()
	 # print(a)
	 # print(type(a))


# print(json.loads(d))
# # print(json.loads(b))  # JSONDecodeError
# print(json.loads(e))