import re

input_str = input("> ")
ans = re.findall(r"\d{4}\/\d{1,2}\/\d{1,2}", input_str)
print(ans)
