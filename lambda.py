# x=lambda x: x+15
# s=x(23)
# print(s)
# y=lambda x,y:x*y
# print(y(3,2))

#######################################
# def func(n):
#     return lambda x: x*n

# result=func(2)
# print(f"the double of number 15 is {result(15)}")

# result=func(3)
# print(f"the triple of number 15 is {result(15)}")

# result=func(4)
# print(f"the quadruple of number 15 is {result(15)}")





#sorting the list of tuple with the second value that is marks here 

# marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# marks=[]
# r=int(input("how many subjects u want to enter: "))
# for i in range(r):
#     s=input("enter the subject name: ")
#     m=int(input(f"enter the marks you got in {s}: "))
#     marks.append((s,m))
# # marks.sort()
# # print(marks)
# marks.sort(key=lambda x: x[1])
# for y,j in marks:
#     print(y,j)




# my_dict=[{'make':'nokia','model':216,'colour':'black'},{'make':'M16','model':2,'colour':'golden'}]
# s=sorted(my_dict,key=lambda x:x['colour'])
# print(s)

# #to filter out the list of even numbers and odd numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x: x%2==0,numbers))
# print(even)
# odd=list(filter(lambda x:x%2==1 ,numbers))
# print(odd)

# #to square and cube every element in the list of integers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# square=list(map(lambda x:x*x,numbers))
# print(square)
# cube=list(map(lambda x:x**3,numbers))
# print(f"cube: {cube}")

# #find that if specific string starts with "p" or not
# s=lambda x: True if x.startswith('p') else False
# print(s("pupil"))

# Write a Python program to extract year, month, date and time using Lambda
# import datetime
# now =datetime.datetime.now()
# year= lambda x: x.year
# month=lambda x: x.month
# day=lambda x:x.day
# ti=lambda x:x.time()
# print(f"the year is: {year(now)}")
# print(f"the month is: {month(now)}")
# print(f"the day is: {day(now)}")
# print(ti(now))

# Write a Python program to create Fibonacci series up to n using Lambda.

l=[]
r=int(input("enter how many digits u want: "))
for i in range(r):
    i=int(input("enter: "))
    l.append(i)
print(l)
s=list(map(lambda x:x+x,l))
print(s)

    
    
   









