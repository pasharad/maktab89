import re

user_input = input('enter your string: ')
pattern = input('enter pattern: ')
ans = re.findall(pattern, user_input)
print(f'{pattern} occured {len(ans)} in your string.')