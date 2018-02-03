# coding:utf-8
class FooClass(object):  # ()中写基类,如object,若无，默认为object
    "FooClass类"
    version = 0.1  # 静态成员

    def __init__(self, nm='John Doe'):  # self相当于Java的this，C#的super，类方法必有参数，nm是默认参数
        "相当于Java的构造方法，C#的构造函数"
        self.name = nm  # 类实例的属性
        print 'Created a class instance for', nm

    def showname(self):
        print 'Your name is', self.name
        print 'My name is', self.__class__.__name__

    def showver(self):
        print self.version
foo1 = FooClass()
print foo1
print foo1.__init__()  # ***打印后有None
print foo1.showname()  # 打印后有None
print foo1.showver()  # 打印后有None

import sys

sys.stdout.write('Hello World!\n')  # （系统）sys模块的打印
sys.stdout.write(sys.platform + '\n')  # 需要\n换行
sys.stdout.write(sys.version + '\n')

# PEP（Python Enhancement Proposal,Python增强提案）索引的网址是http://python.org/dev/peps

print dir(foo1)  # 显示对象属性
number = 1
print dir(number)
print type(number)
print range(1, 3, 1)
print range(2, 10, 2)
# 返回整型列表，range(start,stop,step),start<=整数<stop,step是步长
