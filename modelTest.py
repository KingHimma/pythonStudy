#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'King'

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

print __name__


class TestClass(object):
    """docstring for TestClass"""
    def __init__(self, arg):
        self.__arg = arg
    
    def get_arg(self):
        return self.__arg        

 
# class Student(object):

# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score

#     def get_name(self):
#         return self.__name



king = TestClass('King')
print king.get_arg()


'''
    继承
'''
class Animal(object):
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        print 'Animal is run ...'
        


class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, arg):
        self.arg = arg

    def run(self):
        print 'DOg is run ...'
    

d = Dog(1)
d.run()


print isinstance(d, Animal)
print isinstance(d, Dog)

## 鸭子类型特点   看起来像鸭子，走起路来像鸭子就可以  没有java的强制要求 只要传入进来的有一个run（）方法就ok
def testMain(obj):
    obj.run()

testMain(Animal('1'))
testMain(Dog('1'))


print type(123)
print type(abs)
print type(d)
print dir(d)






