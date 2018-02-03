# coding:utf-8
myString = 'Hello World'
print myString  # 控制台打印

print "%s is number %d!" % ("Python", 1)  # 控制台格式打印

logfile = open('mylog.txt', 'a')  # 'a'表示追加（append）
print >> logfile, 'log:Fatal error:invalid input'  # 文件写入
logfile.close()

user = raw_input('Enter login name:')  # 控制台读入
print 'You login name is:', user  # ,显示空格

num = raw_input('Now enter a number:')
print 'Doubling your number:%d' % (int(num) * 2)  # 类型转换

# help(raw_input)获得函数帮助，***可能报未引用

def foo():  # 方法注释
    "This is a doc string."
    return True
