import re

my_str = "odubhe 12 ovb76 6t7t7 dlfib 878787 kjh87kjh 90 09"
ans = re.findall("\d+", my_str)
# print(ans)
for num in ans:
    print(num, end=" ")
