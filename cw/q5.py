import re

input_date = "2022-12-29"
ans = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', input_date)
print(ans)
