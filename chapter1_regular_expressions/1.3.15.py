'''
1.3.15 杂项
'''
import re
m1 = re.match('\bblow', 'blow')
if m1 is not None:
    print(m1.group())
else:
    print("...1")

# \b 表示边界
m2 = re.match('\\bblow', 'blow')
if m2 is not None:
    print(m2.group())
else:
    print("...2")


m3 = re.match(r'\bblow', 'blow')
if m3 is not None:
    print(m3.group())
else:
    print("...2")


# ...1
# blow
# blow
