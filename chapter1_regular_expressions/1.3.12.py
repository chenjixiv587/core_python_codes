"""
1.3.12 使用sub()和subn()搜索与替换
"""


import re


print(re.sub('X', 'Mr.Smith', 'attn:X\n\nDear X, \n'))
# attn:Mr.Smith

# Dear Mr.Smith,

print(re.sub('X\n', 'Mr.Smith', 'attn:X\n\nDear X, \n'))
# attn:Mr.Smith
# Dear X,

print(re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X, \n'))
# ('attn:Mr.Smith\n\nDear Mr.Smith, \n', 2)

print(re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X, \n')[0])
# attn:Mr.Smith

# Dear Mr.Smith


print(re.sub(r'[ab]', 'x', 'abfgsjjdbsaabba'))
# xxfgsjjdxsxxxxx

print(re.subn(r'[ab]', 'X', 'abhhfhfhfhbaababababab'))
# ('XXhhfhfhfhXXXXXXXXXXXX', 14)


# ---------------------
# 将 MM/DD/YY{,YY} 转变为  DD/MM/YY{,YY}

# 可以将分组顺序替换
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91'))
# 20/2/91


print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991'))
# 20/2/1991
