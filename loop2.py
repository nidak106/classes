responses={}
polling=True
while polling:
    name=input("enter your name: ")
    response=input("which mountain would you like to climb someday? ")
    responses[name]=response
    repeat=input("would u let another person respond: (no/yes) ")
    if repeat=='yes':
        polling=True
    else:
        polling=False          
for name,response in responses.items():
    print(f"{name} would like to climb {response}") 
 
 #example no 2
# students_data={}
# add=True
# while add:
#     student=input("enter your name: ")
#     age=input("enter your age: ")
#     students_data[student]=age
#     repeat=input("are there more students: ")
#     if repeat=='yes':
#         add=True
#     else:
#         add=False            
# for student,age in students_data.items():
#     print(f"{student} has an age of {age}")        
       
