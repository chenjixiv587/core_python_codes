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

print(re.search(
    r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 222-1212').groupdict())
# {'areacode': '800', 'prefix': '222'}
