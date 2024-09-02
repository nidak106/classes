# words=[]
# r=int(input("ennter how many words u have: "))
# for i in range(r):
#     i=input('enter what u want: ')
#     words.append(i)
#     sort=sorted(words)
# print(sort)

# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))
# Prompt the user for input


words=[]
r=int(input("enter how many words u want u write: "))
for i in range(r):
    i=input("enter words: ")
    words.append(i)
    words.sort()
sorted_words='-'.join(words)
print(sorted_words) 
   
  
    