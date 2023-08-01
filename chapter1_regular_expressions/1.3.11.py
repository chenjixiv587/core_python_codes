"""
1.3.11 使用findall()和finditer()查找每一次出现的位置
"""
# findall() 返回的时一个列表  找不到匹配的 就返回空列表
import re

res1 = re.findall(r'car', 'car')
print(res1)
# ['car']

res2 = re.findall(r'car', 'scarrrrry')
print(res2)
# ['car']

res3 = re.findall(r'car', 'carry the barcardi to the car')
print(res3)
# ['car', 'car', 'car']


res4 = re.findall(r'(a(b))', 'abcbdabaabb')
print(res4)
# [('ab', 'b'),('ab', 'b'),('ab', 'b')]

# --------------------------------------------------------

# finditer() 返回的是一个 可迭代对象
# re.I re.IGNORECASE  不区分大小写
s = "This and that This and that"
res5 = re.findall(r'(th\w+) and (th\w+)', s, re.IGNORECASE)
print(res5)
# [('This', 'that'), ('This', 'that')] 是把匹配到的分组都放在一个元组里面


for i in re.finditer(r'(th\w+) and (th\w+)', s, re.I):
    print(i.groups())

# ('This', 'that')
# ('This', 'that')


res6 = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
print(next(res6).group(1))
# This
print(next(res6).group(2))
# That


res7 = [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)]
print(res7)
# [('This', 'that'), ('This', 'that')]


s1 = "This and That"
# 只有两个分组或者以上 返回的列表子元素才是 元组
# this will be a list of tuples if the pattern has more than one group.
res8 = re.findall(r'(th\w+)', s1, re.I)
print(res8)
# ['This','That']


#  只有返回的是 Match[str] 才会有 group() groups()
res9 = re.finditer(r'(th\w+)', s1, re.I)
print(next(res9).groups())
# ('This',)
print(next(res9).groups())
# ('That',)

print([g.group(1) for g in re.finditer(r'(th\w+)', s1, re.I)])
# ['This', 'That']
