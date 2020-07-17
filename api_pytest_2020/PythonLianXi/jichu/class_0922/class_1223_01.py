# age=int(input("请输入年龄: "))
#
# if age>=18:
#     print("恭喜你，你成年了")
# elif 18>age>=0:
#     print("你还太小了 ")
# else:
#     print("你输入有误")

#
#
# l=[[5,6,9,3,7],[1,2,3,4,]]
# for i in l:
#     print(i)
#     for  a in i:
#         print(a)
#
# sum=0
# for i in range(101):
#     sum=sum+i
# print(sum)



# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# def zhengshu(m,k):
#     sum=0
#     for i in range(m,k):
#         sum+=i
#     # print("求和的值是：",sum)
#     return sum
# zhengshu(1,6)
#


#     i=1
#     sum=0
#     while i<=100:
#         sum = sum + i
#         i=i+1
#
#         print("总数",sum)
# zhenghsu(name=100)
#
#

#
# def add_two(a,b):
#     return (a+b)
# print(add_two(1,3))

# def che_list(l):
#     if len(l)>2:
#         new=l[0:2]
#     return new
#
#
# l=[1,2,3,4,5]
# new=che_list(l)
# print(new)




#动态参数/不定长参数*args arguments
# def make_sandwich(*args):
#     # print(*args)
#     all=""
#     for item in args:
#         all=all+item
#         all=all+'.'
#     print("你的包含了这些菜品"+all)
#     return all
# make_sandwich("生菜","菠菜",'土豆')
# make_sandwich("wohaiza")
# lls = (78, 'stupid')
# dds = dict(k1=1, k2=2, k3=3, name='stupid', num=76)
#
# def unpack(**word):
#
#     print('hope stupid..',word.values())
#
#
# unpack(**dds)