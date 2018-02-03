# coding:utf-8
print str(1 / 2)  # 转成字符串型

print str(1 // 2)  # ***未四舍五入

print 1 * 2 + 2 ** 3  # 2**3是2的三次方，即2^3

print 2 < 4 and not (3 > 4 or 1 < 3)

# Python不支持n++，++n,n--,--n

import decimal

print decimal.Decimal('1.1')

python = 'Python'  # 字符串
iscool = 'is cool'
print python[0]
print python[2:4]  # 2<=所取下标<4
print python[:2]  # 所取下标<2
print python[2:]  # 2<=所取下标
print python[-1]
print "'Python is cool'" + '-' * 5 + python + ' ' + iscool

aList = [1, 2, '3', 4]  # 列表，元素重新赋值更改
print str(aList[2:])

aTuple = ('robots', 77, 93, 'try')  # 元组，元素不可重新赋值更改
print str(aTuple[:3])

aDict = {'host': 'earth'}  # 字典，相当于Java的Map
aDict['port'] = 80
print aDict
print aDict.keys()
for key in aDict:  # for in即foreach in
    print key, aDict[key]

expression1 = 1
expression2 = 0
if expression1:
    print 1
elif expression2:  # elif即else if
    print 0
else:
    print 1

while expression1:
    expression1 = expression1 - 1
    print str(expression1)

print 'a',
print 'b'  # ,有空格连接效果，第一、二行的结果与第三行相同，即a b
print 'a', 'b'

for eachNum in [0, 1, 2]:
    print eachNum,
print  # 可换行
for eachNum in range(3):  # range(3)相当于[0,1,2]，eachNum取0，1，2
    print eachNum,
print
foo = 'abc'
for eachNum in range(len(foo)):  # len(foo)得到字符串长度
    print foo[eachNum],
print

sequared = [x ** 2 for x in range(4)]  # 列表解析，4为列表长度，x ** 2得到数组元素
for i in sequared:
    print i,
print

handle = open('mylog.txt', 'r')
# 'r'表示读取（read），'w'表示写入（write），'a'表示追加（append），'+'表示读写，'b'表示二进制访问
# 默认为'r'
for eachLine in handle:
    print eachLine,  # 默认每行文本自带空行，,可减少额外空行
handle.close()

try:
    fobj = open('a.txt', 'r')
except IOError:
    print IOError

def addMe2Me(x):
    "翻倍"
    return x + x

print addMe2Me(10)  # 不同于Java重载，任意参数类型
print addMe2Me('Python')
print addMe2Me([-1, 'abc'])

def foo(debug=True):  # True不能写成true
    if debug:
        return 'debug'
    else:
        return 'done'
print foo()  # 未给参数赋值，则默认参数debug为True
print foo(False)  # False不能写成false
