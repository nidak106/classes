    #to calculate the number of upper and lower cases
def calculate(a):
    i=0
    y=0
    for char in a:
        if char.isupper():
            i+=1
        elif char.islower():
            y+=1      
    return i,y       
print(calculate("Nida Khan is a genius"))     

  