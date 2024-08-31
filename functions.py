def calculategmean(a,b):
    mean =a*b/(a+b)
    print(mean)
def greater(a,b,c):
    if a<b and c<b:
        print("b is greater")
    elif a>b and a>c:
        print("a is greater")  
    elif c>a and c>b:
        print("c is greater ")    
def globe(a):
    i=1
    for y in a:
        i+=y
    return i
# a=8
# b=9
# c=90
# calculategmean(a,b)
# greater(a,b,c)
print(globe((2456789)))