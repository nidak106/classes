#to find the factorial of the number 
def factorial(a):
    if a==0:
        return 1
    else:   
     return a*factorial(a-1)


n=int(input("enter the number: "))
print(factorial(n))