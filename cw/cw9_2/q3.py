import re
user_input = input('enter your string: ')
ans = re.sub(r'\s', '_', user_input)
finall = ''
for i in range(len(user_input)):
    if user_input[i] == '_' and user_input[i] == ans[i]:
        finall += ' '
    else:
        finall += ans[i]
print(finall)