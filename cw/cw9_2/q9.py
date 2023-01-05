import re

input_str = "aif54 s80tbh5 543 iufg 34 8 jk"
ans = re.findall("\d+", input_str)
temp = list(re.finditer("\d+",input_str))
for i in range(len(temp)):
    print(ans[i],"\t",temp[i].span())
