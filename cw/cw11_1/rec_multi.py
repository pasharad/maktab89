def mult(a, b):
    if a == 0:
      return 0
    elif a == 1:
      return b
    else:
      return b + mult(a-1, b)
  
a=float(input("Enter a:"))
b=float(input("Enter b:"))
print(mult(a,b))