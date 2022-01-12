import numpy
# class MyClass: 
#    a = '123' 
#    def __init__(self, a=0): 
#        self.a = 'None' 


# a=MyClass()
# b=MyClass()
# print(issubclass(MyClass,MyClass)) 
# print(isinstance(a, type(b))) 
# print(dir(a) == dir(b))
# print(a==b)
# print(dir(a) is dir(b))

# class Class1: 
#     a = '1' 
#     def __init__(self, a): 
#         Class1.a = self.a*a
# el = Class1(2)
# el2 = Class1(2)
# print(el.a+el2.a)


# class MyClass: 
#     __val = -5    
#     def __init__(self): 
#         self.__val=5
#     def pr(self):
#         print(self.__val)
# a = MyClass()
# a.pr()

# class MyClass: 
#     def __init__(self): 
#         self.__val = 0
#     def pr():
#         print(self.__val)
# a = MyClass()
# a.__val=10
# a.pr()


# class MyClass:
#     @staticmethod
#     def m1 (p):
#         print(p)
#     def _m2(self, p):
#         print(p) 
#     @staticmethod
#     def m3(self, p):
#         print(p)
#     def m4(p):
#         print(p) 
#     def ___m5(self, p):
#         print(p) 
# c = MyClass()


# c.m1(1)
# c._m2(1)
## c.m3(1)
## c.m4(1)
# c.__m5(1)

# class MyClass():
#     var = 10
#     def __init__(self, val=0): 
#         self.var = val
# c = MyClass(-2)
# d = MyClass(c)
# print(d.var)


# class MyClass:
#     def add(self, p, n):
#         return p + n
#     def pr(self, x):
#         a = self.add(x, 2)
#         print(a)
# o = MyClass()
# o.pr(1)

# class MyClass:
#     def met1(self, param):
#         return param * 2
#     def met2 (param):
#         return param * 2
#     @staticmethod
#     def met3(param):
#         return param * 2  
#     def _met4(self, param):
#         return param * 2    
#     def __met5(self, param):
#         return param * 2  
# o = MyClass()
# # print(o.met1(2))

# print(o.__met5(1))

# class Class1():
#     var = 10
#     def __init__(self, val=0): 
#         self.var = val
# c = Class1()
# d=str(type(c)).split('.')[-1][:-2]
# print(d)

# class A:
#     def __init__(self): 
#         self.a = 1
#         self.b = 10
#     def pr(self):
#         print(self.a, self.b)
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.a = 2 
# el1 = B()
# el1.pr()


# class A(object): 
#     def a(self): return 'a'
# class B(object): 
#     def b(self): return 'b'  
# class C(object): 
#     def c(self): return 'c'  
# class AB(A, B): 
#     def a(self): return 'ab'
# class BC(B, C): 
#     def a(self): return 'bc'
# class ABC(AB, B, C): 
#     def a(self): return 'abc'

# li = [-9, -16, 2, 91]
# x1 = all(min(y) for y in enumerate(li,-3))
# x2 = any(min(y) for y in enumerate(li,-3))
# x = x1 and x2
# print(x)

# itr = iter(sorted('PYTHON'))
# i = 0
# while i<6:
#     next(itr)*2
#     i += 2
# print(''.join(list(itr)))


# print(numpy.shape(numpy.array([[1, 2], [3, 4], [5, 6]])))

# print(numpy.size(numpy.ones((2, 5))))

# import queue
# q = queue.LifoQueue()
# for i in range(4):
#     q.put(i*2+1)
# while not q.empty():
#     print(q.get(), end=' ')


# myStack = []
# a = [1, 2, 3]
# myStack.append('31')
# myStack.append(a)
# myStack

# print(myStack)

# import queue
# q = queue.Queue()
# for i in range(3, 9):
#     q.put(10+i)
# while not q.empty():
#     print(q.get(), end=' ')

# def LowerBound(A, key): 
#     left = -1 
#     right = len(A) 
#     while right > left + 1: 
#         middle = (left + right) // 2 
#         if A[middle] >= key: 
#             right = middle 
#         else: 
#             left = middle 
#     return right
# A=[11,21,38,32,53,6]
# key=32
# print(LowerBound(A, key))

# def f(x, y, z, a=None, b=None):
#     print (x, y, z, a, b)
# f(*[1, 2, 3], *{'a': 4, 'b': 5})


# def addClosure(val1):
#     def closure(val2):
#         return val1 + val2
#     return closure
# class AddFunctor(object):
#     def __init__(self, val1):
#         self.val1 = val1
#     def __call__(self, val2):
#         return self.val1 + val2
# cl = addClosure(3)
# fn = AddFunctor(-3)
# print (cl(cl(-3)), fn(fn.__call__(2)))

# class A(type):
#   def __init__(cls, name, bases, dict):
#     return super(A, cls).__init__(cls, name, bases, dict)
# B = A("B", (), {})
# print(B)

# def data(d=[1]): 
#     d.append(2) 
#     return d 
# a=data()
# b=data()
# c=data([3])
# print(b,c)


# x = ['a', 'b', 'c', '2']
# y = list(map(lambda x: chr(ord(x) + 1) , x))
# print(y)


# sw = ["в", "и", "по", "за"]
# sw.extend(list(map(lambda x:x.swapcase(), sw)))
# s1 = "Вчера ЗА обедом КАК И позавчера мы решили, и в 19 вечера я и мои друзья отправились по делам за семь холмов и вернулись ночью."
# l1 = s1.split()
# fs = '-'.join((filter(lambda s: s in sw, l1)))
# print(fs)

# list1 = [] 
# list2 = [] 
# for i in range(0,11): 
#     list1.append(4*i)  
# for i in range(0,10): 
#     list2.append(list1[i]%5==0)
# print(any(list2) and not(all(list2)))
# import functools
# numbers = [2, 3, 4, 5, 6]
# print(functools.reduce(lambda res, x: res*x, numbers, 1))


# from functools import reduce
# s = "0av#12+34#0  6"
# v = reduce(lambda x, y: x+len(y), filter(None, s.split(" ")), 4)
# print(v)
# lst = [[1, 5, 3], [0, -3, 4], [0, 1, 4, 1], [0, 7]]
# t1 = max(map(lambda x: x[-2], filter(lambda x: len(x)>2, lst))) 
# t2 = min(map(lambda x: x[-2], filter(lambda x: len(x)>2, lst)))
# t = t2-t1
# print(t)


# def search(A, key):
#     i = 0
#     while i < len(A) and A[i] != key:
#         i += 1
#     if i < len(A):
#         return i
#     else:
#         return -1
# A=[11,21, 38,32,53,6]
# key=40

# print(search(A, key))

# def LowerBound(A, key): 
#     left = -1 
#     right = len(A) 
#     while right > left + 1: 
#         middle = (left + right) // 2 
#         if A[middle] >= key: 
#             right = middle 
#         else: 
#             left = middle 
#     return right
# A=[11,21,38,32,53,6]
# key=32
# print(LowerBound(A, key))

# def push(self, x):
    # self.length+=1
    # if self.first == None:
    #     self.last = self.first = Node(x,None)
    # else:
    #     self.first = Node(x,self.first)


class Table:
    def __init__(self, l, w, h=10):
        self.length = l
        self.width = w
        self.height = h
class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p     
class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = KitchenTable(10,10)
# t2 = KitchenTable(5)
t3 = DeskTable(*(1,2))
t4 = KitchenTable(1, 2, 3)
# t5 = DeskTable(0)

