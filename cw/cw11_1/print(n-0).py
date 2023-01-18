def countdown(n):
    print(n) 
    if n == 0:
        return 0
    return countdown(n - 1)

n=int(input("Enter n : "))
countdown(n)