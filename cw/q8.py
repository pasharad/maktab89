import re

input_str = "ali erfan mamad Amin pasha saleh ehsan abcd efg rtb idbh Aiu"
ans = re.findall(r"\be[A-z]+|\ba[A-z]+",input_str)
print(ans)