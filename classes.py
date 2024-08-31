# class Person:
#     def __init__(self):   #this is how u create a constructor
#         print("hello world")
# Person ()        
     
     
 #this method is used when we pass single values on our own    ,notice only self parameter is passed  
# class Person:
#     def __init__(self):
#         self.age=21
#         self.name="nida"
# person1=Person() 
# print(person1.age)       
# print(person1.name)    

class Person:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def __str__(self):
        return " name : {} ,age: {}, weight: {}".format(self.name,self.age,self.weight)
            
        
#here is a destructor
    def __del__(self):
        print("object deleted")    
        
person1=Person("nida khan",21,46)
print(person1)
# print(f"my name is {person1.name}")
# print(f"I am {person1.age}")
# print(f"I weigh {person1.weight} kg's")
del person1    


