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




##########################################

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
###########################################



# my_dict=[{'make':'nokia','model':216,'colour':'black'},{'make':'M16','model':2,'colour':'golden'}]
# s=sorted(my_dict,key=lambda x:x['colour'])
# print(s)

#to filter out the list of even numbers and odd numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x: x%2==0,numbers))
# print(even)
# odd=list(filter(lambda x:x%2==1 ,numbers))
# print(odd)

#to square and cube every element in the list of integers
numbers=[1,2,3,4,5,6,7,8,9,10]
square=list(map(lambda x:x*x,numbers))
print(square)
cube=list(map(lambda x:x**3,numbers))
print(f"cube: {cube}")




