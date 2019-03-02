'''
str = "今天是非常棒的一日，我很开心！"
print(str[0:-2],end="")
print(str[2:5])
print(str[3:])
'''
'''
a=b=c=1
print(c)
b=2
print(b)
print(a)
c=3
print(c)
print(b)
'''
'''
a=10
b=10
print(a is b)
b=20
print(a is b)
'''

'''
def myFunction(a,*vart,b):
    print("a=",a)
    print("b=",b)
    print("其余：")

myFunction(1,3,b=2)
'''

a = 10
def test(a):
    a = a + 1
    print("test函数内，a=",a)
test(a)
print("test函数外，a=",a)