def reverse(string):
    if len(string)<1:
        return 
    else:
        temp=string[0]
        reverse(string[1:])
    print(temp,end='')

string='milad hastam az maktab89'
reverse(string)
    

    