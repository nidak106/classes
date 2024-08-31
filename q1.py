#to reverse the given string 
def  reverse(a):
    rvr=''
    index=len(a)
    while index>0:
        rvr+=a[index-1] 
        index=index-1
    return  rvr 
n=reverse("nida")
print(n)



            