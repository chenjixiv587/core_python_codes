import re

# . 匹配(match)除了 \n 空字符串以外的字符

anyend = '.end'


def match_end(pattern: str, checked_str: str):
    m = re.match(pattern, checked_str)
    if m is not None:
        return m.group()


match_res = match_end(pattern=anyend, checked_str="\nend")
print(match_res)


# checked_str="bend"   match_res=bend
# checked_str="end"   match_res=None
# checked_str="\nend"   match_res=None

def search_end(pattern: str, checked_str: str):
    m = re.search(pattern, checked_str)
    if m is not None:
        return m.group()


print(search_end('.end', 'the end.'))
# end


# -------------------------------------------------------------


patt314 = '3.14'
pi_patt = '3\.14'

# 精准匹配 \. 就表示的是 . 本身
m = re.match(pi_patt, '3.14')
if m is not None:
    print(m.group())

# . 号匹配 0
m1 = re.match(patt314, '3014')
if m1 is not None:
    print(m1.group())


# . 号匹配 .

m2 = re.match(pi_patt, '3.14')
if m2 is not None:
    print(m2.group())
