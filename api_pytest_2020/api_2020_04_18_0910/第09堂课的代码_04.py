#元组的  不定长参数      *args
def printinfo(*args):
    print("传入的参数：{}".format(args))
c=(1,2,3,4,5,6)
#下面这两种情况 第一种是 实参通过键值传值给形参   第二支是 通过变量赋值进行传值   但是要  *c
printinfo(3, 4)
printinfo(*c)



def func(**kwargs):
	print("不定长参数：{}".format(kwargs))  #字典的可变参数 返回一定要穿kwargs

h = {
    "a1": "xxxxxxxxx",
    "b1": "ssssssssss",
    "c1": "2222222222"
}
#下面这两种情况 第一种是 实参通过键值传值给形参   第二支是 通过变量赋值进行传值但是要  **h
func(b=1,a=2,c=789)
func(**h)



#这种情况下是 传两种类型的,a这个优先考虑实参的
def prin(a,*args,**kwargs):
	print("传入的参数：{},{},{}".format(args,kwargs,a))
prin(1,2,3,b=4,c=5)





def login(username, psw):
    print(username)
    print(psw)
    return "token"


login(username="x123", psw="x456")

s = {
    "username": "x789",
    "psw": "x987"
}
login(**s)