#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Student(object):
	pass

a = Student()
a.name = 'Student King'

print a.name

def set_age(self, age):
	self.age = age
from types import MethodType

a.set_age =  MethodType(set_age, a)
a.set_age(54)

print a.age
## 绑定后只在当前实例a中生效  如果需要所有都生效，可以直接针对于class绑定
Student.name = 'Class name'
a = Student()
b = Student();
print (a.name, b.name)
Student.set_age = set_age
a.set_age(100)
print a.age

## 使用__slots__
## __slots__变量，来限制该class实例能添加的属性：
class SlotsTest(object):
	__slots__ = ( 'name', 'age')

a = SlotsTest()
a.name = 'name'
a.age = 'age'
#a.sex = '男'

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

def split():
	print '--------------------------------------------------------------------------------------------------------------'


split()

class Book(object):
	
	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def weight(self):
		return self._weight


b = Book()
b.height = 100  ## height 可读写
# b.weight = 123  weight 可读
print (b.height)

split()


from Hello import Hello
h = Hello()
h.hello('King')
print type(h)

def fn (selfm ,name = 'world'):
	print ('hello,%s.'%name)


Hello = type('Hello',(object,),dict(hello = fn))  # 创建Hello class
'''
建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''

h = Hello()
h.hello()

print type(Hello)
print type(h)



## TODO  使用元类未理解


	









