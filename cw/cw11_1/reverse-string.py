def reverse(string):
    if len(string) == 0:
        return
     
    t = string[0]
    reverse(string[1:])
    print(t, end='')
 
string = "milad hastam az maktab89"
reverse(string)