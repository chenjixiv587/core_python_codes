"""
1.3.9 重复、特殊字符以及分组
"""
import re
# chenwei@www.xxx.com
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print(m.group())

# nobody@www.xxx.com
# unterminated 未结束的

# --------子组
# () 是为了分组 注意下标从1开始
m1 = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m1.group())
# abc-123
print(m1.group(1))
# abc
print(m1.group(2))
# 123
print(m1.groups())
# ('abc', '123')

# ----- 2 个子组
m2 = re.match('(a)(b)', 'ab')
print(m2.group())
print(m2.group(1))
print(m2.group(2))
print(m2.groups())

# ab
# a
# b
# ('a', 'b')


# ----嵌套的子组

m3 = re.match('(a(b))', 'ab')
print(m3.group())
print(m3.group(1))
print(m3.group(2))
print(m3.groups())

# ab
# ab
# b
# ('ab', 'b')
