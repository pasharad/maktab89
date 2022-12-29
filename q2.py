import re
user_input = input('enter your string: ')
pattern = input('enter your pattern: ')
anwser = []
occ = 0
tmp = re.findall(pattern, user_input)
for i in range(len(tmp)):
    ans = re.search(pattern, user_input).span()
    occ += 1
    user_input = user_input[ans[1]:]
    anwser.append(ans)
print(f'{pattern} occured {occ} and location is {anwser} ')