import re

base_str = 'bit'

pattern = 'bit|bat|bet'


# re.match
# Try to apply the pattern at the start of the string, returning a Match
# object, or None if no match was found.

def match_str(ori_str: str, match_pattern: str):
    m = re.match(match_pattern, ori_str)
    if m is not None:
        return m.group()


res_match = match_str(ori_str=base_str, match_pattern=pattern)
print(res_match)

# bit

print(match_str(ori_str='he bet me', match_pattern=pattern))
# None

# ---------------------------------

# re.search
# Scan through string looking for a match to the pattern, returning a Match
# object, or None if no match was found.


def search_str(ori_str: str, search_pattern: str):
    m = re.search(search_pattern, ori_str)
    if m is not None:
        return m.group()


res_search = search_str(base_str, pattern)
print(res_search)

# bit


print(search_str(ori_str='he bet me', search_pattern=pattern))
# bet
