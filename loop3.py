import time
sandwitches=[]
finished_sandwitches=[]
s=int(input("how many sandwitches u want to order: "))
for i in range(s):
    y=input("enter sandwitches: ")
    sandwitches.append(y)
    
while sandwitches:
    n=sandwitches.pop()
    finished_sandwitches.append(n)
    print(f"we are preparing your {n}") 
    time.sleep(1.5)  
    
print("take your order")


        
        
