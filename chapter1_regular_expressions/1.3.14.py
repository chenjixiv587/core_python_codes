"""
1.3.14 扩展符号
"""
# (?iLmsux) 在正则表达式中 嵌入一个或者多个特殊‘标记’参数（或者通用函数、方法） iLmsux 等都是特殊标记
import re
# (?i) 忽略大小写
print(re.findall(r'(?i)yes', 'yes? YES.yEs!'))
# ['yes', 'YES', 'yEs']

print(re.findall(r'(?i)th\w+', 'The quickest way to through This lesson is practising.'))
# ['The', 'through', 'This']
# -----------------------------------------------------------------------------------------------


# (?im) 跨行搜索 忽略大小写
print(re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line,it is the best
"""))
# ['This line is the first', 'that line']

# --------------------------------------------------------------------------------

print(re.findall(r'th.+', """
This line is the first,
another line,
that line,it is the best
"""))
# ['the first,', 'ther line,', 'that line,it is the best']

# (?s) . 号匹配任意字符
# re.X re.DOTALL
print(re.findall(r'(?s)th.+', """
This line is the first,
another line,
that line,it is the best
"""))
# ['the first,\nanother line,\nthat line,it is the best\n']


# -------------------------------------------------------
# re.X re.VERBOSE 用来去除多行显示正则表达式时的空白符
# 简单来说就是 忽略掉规则中的空白符 而用 [] 来显式表示空白符
# (?x)
pattern = r"""(?x)
\((\d{3})\) # 区号
[ ] # 空白符 需要显式展示
(\d{3}) # 前缀
- # 横线
(\d{4}) # 终点数字
"""
print(re.search(pattern, '(800) 555-1212').group())
# (800) 555-1212
print(re.search(pattern, '(800) 555-1212').groups())
# ('800', '555', '1212')


# -------------------------------
# (?:xxxx) 对部分表达式进行分组，但是并不会保存这个分组作为以后被调用或者使用
print(re.findall(r'(?:\w+\.)*(\w+\.com)',
                 'http://google.com http://www.google.com http://code.google.com'))
# ['google.com', 'google.com', 'google.com']


# ---------------------------------------
# 使用名称标识符来表示对应的分组 而不是用 1 2 3 等等表示
# (?P<name>)
# (?P=name)

print(re.search(
    r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 222-1212').groupdict())
# {'areacode': '800', 'prefix': '222'}


print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
             r'(\g<areacode>) \g<prefix>-xxxx', '(800) 222-1212'))
# (800) 222-xxxx


# ----------

# (800) 123-1212
print(bool(re.match(
    r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)',
      '(800) 222-1212 800-222-1212 18002221212')))
# True

# 更优雅的方式
print(bool(re.match(r'''(?x)
         \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
         [ ]
         (?P=areacode)-(?P=prefix)-(?P=number)
         [ ]
         1(?P=areacode)(?P=prefix)(?P=number)
''', '(800) 222-1212 800-222-1212 18002221212')))
# True
# ------------------------------------------------
# (?=xxx) 正向前视断言 就是说只获取最靠近 xxx 的前面的直接的东西
# (?!xxxx) 正向负视图断言 将 xxx 剔除
print(re.findall(r'\w+(?= van Rossum)', '''
          Guido van Rossum
           Tim Peters
           Alex Materlli
           Just van Rossum
           Raymond Hettinger      
'''))
# ['Guido', 'Just']

print(re.findall(r'(?m)\s+(?!noreply|postmaster)(\w+)', '''
           sales@jswodun.com
           postmaster@jswodun.com
           eng@phptr.com
           noreply@phptr.com
           admin@phptr.com   
'''))
# ['sales', 'eng', 'admin']


print(['%s@bruce.com' % e.group(1) for e in
       re.finditer(r'(?m)\s+(?!noreply|postmaster)(\w+)', '''
           sales@jswodun.com
           postmaster@jswodun.com
           eng@phptr.com
           noreply@phptr.com
           admin@phptr.com   
''')
       ])
# ['sales@bruce.com', 'eng@bruce.com', 'admin@bruce.com']


# ---------条件判断
print(bool(re.search(r'(?:(x)|y)((?(1)y|x))', 'xy')))
#  True
