# coding:utf-8
print int(raw_input('Enter number:'))

# 输出1至10
for num1 in [x for x in range(0, 11, 1)]:
    print num1,
print
num2 = 0
while num2 <= 10:
    print str(num2),
    num2 = num2 + 1

# 正负零判断
print
num3 = int(raw_input('Enter number:'))  # raw_input('Enter number:')与0比较会转成ASCII码
if num3 < 0:
    print '负数'
elif num3 == 0:
    print '零'
else:
    print '正数'

# 输出字符
num4 = 0
string1 = raw_input('Enter string:')
while num4 < len(string1):
    print string1[num4],
    num4 += 1
print
for char in string1:
    print char,

# 求五个数和
numList1 = range(0, 5, 1)
for num5 in range(0, 5, 1):
    numList1[num5] = int(raw_input('第' + str(num5 + 1) + '个数：'))
sum = 0
for num6 in numList1:
    sum += num6
print sum

# 求五个数和
numList2 = range(0, 5, 1)
num6 = 0
while num6 < 5:
    numList2[num6] = int(raw_input('第' + str(num6 + 1) + '个数：'))
    num6 += 1
sum = 0
num7 = 0
while num7 < 5:
    sum += numList2[num7]
    num7 += 1
print sum

# 求五个数平均数
numList1 = range(0, 5, 1)
for num5 in range(0, 5, 1):
    numList1[num5] = int(raw_input('第' + str(num5 + 1) + '个数：'))
sum = 0
for num6 in numList1:
    sum += num6
print float(sum) / 5  # float(sum)/5相当于sum * 1.0  / 5

# 输入1至100的数
alert = False
while alert == False:
    num = int(raw_input('Enter number(1<=number<=100):'))
    if (num >= 1 and num <= 100):
        print 'Success'
        alert = True
    else:
        print 'Fail'

def getSum():
    numList1 = range(0, 5, 1)
    for num5 in range(0, 5, 1):
        numList1[num5] = int(raw_input('第' + str(num5 + 1) + '个数：'))
    sum = 0
    for num6 in numList1:
        sum += num6
    print sum

def getAverage():
    numList1 = range(0, 5, 1)
    for num5 in range(0, 5, 1):
        numList1[num5] = int(raw_input('第' + str(num5 + 1) + '个数：'))
    sum = 0
    for num6 in numList1:
        sum += num6
    print float(sum) / 5

alert = False
while alert == False:
    item = raw_input('（1）求五个数的和（2）求五个数的平均值（X）退出：')
    if item == '1':
        getSum()
    elif item == '2':
        getAverage()
    elif item == 'X':
        alert = True

strList = ['a', 'b', 'c', 'd']
for strListItem in strList:
    print dir(strListItem)

print type(dir)
print type(int)
print type(1)
print type('1')

print dir.__doc__

import sys

print dir(sys)
sys.exit()

# 冒泡排序
num1 = int(raw_input('Enter number;'))
num2 = int(raw_input('Enter number;'))
num3 = int(raw_input('Enter number;'))
numList = [num1, num2, num3]
for numOut in range(0, len(numList) - 1, 1):
    for numIn in range(0, len(numList) - numOut - 1, 1):
        if not (numList[numIn] < numList[numIn + 1]):
            a = numList[numIn + 1]
            numList[numIn + 1] = numList[numIn]
            numList[numIn] = a
for num in numList:
    print num,
print
for numOut in range(0, len(numList) - 1, 1):
    for numIn in range(0, len(numList) - numOut - 1, 1):
        if not (numList[numIn] > numList[numIn + 1]):
            a = numList[numIn + 1]
            numList[numIn + 1] = numList[numIn]
            numList[numIn] = a
for num in numList:
    print num,
