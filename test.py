# -- coding: utf-8 --

print '你好'
print ('hello,World')
print ('1','2','3','4')
print ('The quick brown fox', 'jumps over', 'the lazy dog')

print '''line1
line2\nline3'''


print r'''line1
line2\nline3'''
# name = input( '请输入name = ' )
# print name


print True

print 10 > 2
print not 100 > 23

print 10 * 3


customlist = ['1','2','3']
print customlist

# age = input('age = ')

# if age < 9:
# 	print 'age >  9 --- >' + age
# else:
# 	print '未知'
# customlist = range(10)
# sum = 0
# for x in customlist:
# 	sum += x
# 	if x == 5:
# 		continue
# 	print x

# print sum

# cmap = {"k":1,"a":2,'k':3}
# print cmap['k']
# print cmap.get('4',4)


# def function(x,y=3):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('参数错误')
# 	return x + y,x,y

# print function(9)

# def fact(x):
# 	if x == 1:
# 		return 1
# 	return x * fact(x-1)
# print fact(100)


# customlist = range(100)

# print customlist[0:89]
# print customlist[-3]


#切片
L = list(range(100))
print L
print L[-10:]
## 前十个数，每两个取一个
print L[:10:2]

print L[::5]
print 'asdfghmasdfghmasdfghmasdfghm'[:10]

## 列表表达式
print [x*x for x in range(10)]


def add(x,y):
	return x + y

def remove(x,y):
	return x - y

f = remove(80,add(10, 2+8))


print remove.__name__

# def debug(func):
#     def wrapper():
#         print "[DEBUG]: enter {}()".format(func.__name__)
#         return func()
#     return wrapper

# @debug
# def say_hello():
#     print "hello!"
# say_hello()

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging (level = 'ERROR')
def say(something):
    print "hello {}!".format(something)

say("123456")

print int("10",2)

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

def fmap(x):
    return x * x

print list(map(fmap, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

## 匿名函数
print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


listTest = list(range(10))


import functools
## functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base = 2)

print int2('10000')

print sys.path



