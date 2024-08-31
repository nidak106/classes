#print the even numbers in the list 
def even(n):
    ev=[]
    for i in range(0,len(n)+1):
        if i %2==0:
            ev.append(i)
    return ev
print(even((1,2,3,4,5,6,7,8,9,10)))



        
    