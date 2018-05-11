# class Human(object):
#     def __init__(self, name, age, tel):
#         self.__name = name
#         self.__age = age
#         self.__tel = tel
#
#     def getname(self):
#         return self.__name
#     def getage(self):
#         return self.__age
#     def gettel(self):
#         return self.__tel
#
# m = Human('tom', 45, '123333333333')
# print(m.getname())
# print(m.getage())


# def print_triangle(n):
#     for i in range(1, n +1):
#         for j in range(n - i):
#             print(' ',end='')
#         for j in range(2 * i-1):
#             print('*',end='')
#         print()
#
# print_triangle(3)


# def fibs(n):
#     Fib = []
#     Fib.append(1)
#     Fib.append(1)
#     for i in range(2, n):
#         val=getFibVal(Fib[i-1], Fib[i-2])
#         Fib.append(val)
#     return Fib
#
# def getFibVal(num1, num2):
#     return num1 + num2
#
# print(fibs(5))


# def fibs(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fibs(n-1)+fibs(n-2)
#
# def fibList(n):
#     list1 = []
#     for i in range(n):
#         list1.append(fibs(i))
#     return list1
#
# list1 = fibList(5)
# print(list1)

# L = [1,2,3,4,5,6,7,8,9]
# print([x for x in L if x % 3 ==0])

list1 = [1]
def fibs(n, i, a, b):
    a, b = b, a + b
    list1.append(b)
    i += 1
    if n > i:
        fibs(n, i, a, b)
    if n == i:
        return list1

L = fibs(10, 1, 0, 1)
print(L)


# def mysplit(str1, splitChar = ' '):
#     list1 = str.split(str1, splitChar)
#     return list1
#
# L = mysplit('name#age', '#')
# print(L)


# def fun(lst):
# 	l2 = lst
# 	l2 = [max(lst)]
# 	return l2
#
# l = [1,2,3]
# fun(l)
# print(l)
# l = fun(l)
# print(l)


# for i in range(2):
# 	for j in range(3):
# 		if j == 2:
# 			break
# 		print(i, j)



# d = {}
# l2 = ['a','b','c']
# l3 = [1,2,3]
# i = 0
# while i<3:
# 	d[l2[i]] = l3[i]
# 	i += 1
# print(d)


# def myyield():
#     print("2…")
#     yield   2
#     print("3…")
#     yield   3
#     print("5…")
#     yield   5
#     print("7…")
#     yield   7
#     print("end")
# it = iter(myyield())
# print(next(it))

#
# def fun(a,b):
#     def f():
#         return a+b
#     return f
#
# f1 = fun(100, 200)
#
# print(f1())


# def decdsso(fn):
#     print("decdsso")
#     def f2():
#         print("f2")
#     return f2
#
# @decdsso
# def myfunc():
#      print("myfun!")
# myfunc()



# x = {'a':'b', 'c':'d'}
# print(set([1, 1, 2, 3]))
# print(1, 2, 3, sep=':')

# x = [1,2,3]
#
# x.insert(0, 3)
# print(x)


# f = lambda x: 5
# print(f(3))

# print(sorted([1, 2, 3], reverse=True))  #  == reversed([1, 2, 3])
# print(reversed([1, 2, 3]))

# print(list(map(str, [1, 2, 3])))

# import random
#
# x = [1,2,3,4]
# print(random.choice(x))