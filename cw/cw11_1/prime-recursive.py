def Prime_Number(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
        
    return Prime_Number(n, i + 1)


n=int(input("enter n : "))
if Prime_Number(n):
    print( n, "is Prime")
else:
    print( n, "is not a Prime")