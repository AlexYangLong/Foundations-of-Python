'''
title: 类方法 、静态方法
time: 2018.04.12 16:07
author: 杨龙（Aelx）
'''
'''
普通方法:1.至少有一个参数,表示当前对象,
类方法:1.至少有一个参数, 表示当前类
静态方法:1.默认没有参数
'''

class Class(object):
    def normalMethod(self):
        print('这是普通方法')

    @classmethod
    def classMethod(cls):
        print('这是类方法')

    @staticmethod
    def staticMethod():
        print('这是静态方法')

c1 = Class()
c2 = Class()

# normalMethod通过class去调用或者通过实例化后的对象去调用,对于实例化后产生的对象是不一样的,所以最后调用的方法的内存地址也是不一样.  而使用类名去调用普通方法,是属于没有被对象绑定的方法
print(Class.normalMethod)
print(c1.normalMethod)
print(c2.normalMethod)

print('#'*40)
# 无论是通过类调用还是通过不同的对象去调用,最终的结果都是一样,也就是他们都指向同一块内存地址
print(Class.classMethod)
print(c1.classMethod)
print(c2.classMethod)

print('#'*40)
# 静态方法无论是通过class还是通过不同的对象去调用,最终的结果都是一样的,即都是指向同一块内存地址.也就是说,静态方法无论通过类还是对象去调用,一旦调用,则内存地址就确定
print(Class.staticMethod)
print(c1.staticMethod)
print(c2.staticMethod)






