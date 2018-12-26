#!/user/bin/env python3
#-*- coding: utf-8 -*-


# 切片
# 操作对象：list、tuple、string -- 返回对应类型
L = list(range(100))
print(L)
print(L[:])
# 输出：[0, 1, 2, 3, ..., 98, 99]

# 取 前 3 个元素
print(L[0:3])
# 输出：[0, 1, 2]
print(L[:3])        # 省略写法
# 输出：[0, 1, 2]

# 从索引 1 开始，取出两个元素
print(L[1:3])
# 输出：[1, 2]

# 取出后10至倒数第二个数
print(L[-10:-1])
# 输出：[90, 91, 92, 93, 94, 95, 96, 97, 98]

# 取出后10个数
print(L[-10:])
# 输出：[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# 取前 10 个数，每两个去一个
print(L[:10:2])
# 输出：[0, 2, 4, 6, 8]

# 所有数，每五个取一个
print(L[::5])
# 输出：[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# tuple
print((0, 1, 2, 3, 4, 5)[:3])
# 输出：(0, 1, 2)

# string
print("ABCDEFG"[:3])
# 输出：ABC


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

# 循环
def trim(s):
    while len(s)>0 & s[0]=='':
        s=s[1:]
    while len(s)>0 & s[-1]=='':
        s=s[:-1]
    return s

# 递归
def trim1(s):
    if len(s)==0:
        return s
    if s[0]==' ':
        return trim1(s[1:])
    if s[-1]==' ':
        return trim1(s[:-1])
    else:
        return s