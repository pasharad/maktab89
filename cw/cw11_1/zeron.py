
def countdown(n):
    
    if n>=1: 
        countdown(n-1)  
    print(n, end=" ")

n=int(input("Enter n:"))

countdown(n)