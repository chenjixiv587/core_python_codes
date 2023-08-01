"""
1.3.10 匹配字符串的起始和结尾以及单词边界
边界类更多表示的是位置 一般用于表示搜索而不是匹配
"""
import re


m1 = re.search('^The', 'The day')
if m1 is not None:
    print(m1.group())
    # The
else:
    print("No Thing.")


m2 = re.search('^The', 'end The')
if m2 is not None:
    print(m2.group())
else:
    print("No Thing")
# No Thing

# ** 在通常情况下， 在正则表达式里面 使用原始字符串是个好主意 **
# --- \b 是边界 就是前面有空格等

m3 = re.search(r'\bThe', 'The end')
if m3 is not None:
    print(m3.group())
# The


m4 = re.search(r'\bThe', 'bywayThe')
if m4 is not None:
    print(m4.group())
else:
    print("No Thing")
# No thing


# -----\B 没有边界(在一个单词的最后是没有边界的)
m5 = re.search(r'\BThe', 'DogcatThe')
if m5 is not None:
    print(m5.group())
else:
    print("No thing")
# The
