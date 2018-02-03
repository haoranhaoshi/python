# Python变量不需事先声明，也无需类型声明

# Python引用计数增加：
x = 3  # 0->1，引用计数（指向对象3的指针数量）加1
y = x  # 引用计数加1

def foo(a):
    print a

foo(x)  # 引用计数加1
myList = [123, x]  # 引用计数加1
# 追踪调试对象引用计数加1

# Python引用计数减少（对应增加）：
x = 4  # 引用计数减1
del y  # 引用计数减1
# 函数运行结束，引用计数减1
myList.remove(x)  # 引用计数减1
del myList  # 引用计数减1
del x  # 引用计数减1
