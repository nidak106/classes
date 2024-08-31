def perfect_num(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
    return sum==a  
print(perfect_num(6))        
