"""
1.3.13 在限定模式上使用split()分隔字符串

"""
import re
DATA = (
    'Mountain View, CA 94040', 'Sunnyvale, CA', 'Los Altos, 94023', 'Cupertino 95014', 'Palo Alto CA'
)
for datum in DATA:
    # 通常这样说：如果空格紧跟在五个数字（ZIP编码）或者两个大写字母（美国联邦州缩写）之后，
    # 就用split语句分割该空格。这就允许我们在城市名中放置空格。
    print(re.split(r', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

# ['Mountain View', 'CA', '94040']
# ['Sunnyvale', 'CA']
# ['Los Altos', '94023']
# ['Cupertino', '95014']
# ['Palo Alto', 'CA']


# -------知识点
# (?=xxx) 匹配条件是  如果xxx出现在之后的位置，而不使用输入字符串，叫做 正向前视断言
# (?:xxx) 匹配条件是 表示一个匹配不用保存的分组
