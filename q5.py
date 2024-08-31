#to check whether the number is prime or not 
def prime(n):
    if n==1:
        return "not a prime"
    for i in range(2,n):
        if n%i==0:
            return "not a prime"
    return "prime"    
print(prime(34))              
        
        