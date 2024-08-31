def palindrome(n):
    rvr=''
    index=len(n)
    while index>0:
        rvr+=n[index-1]
        index=index-1
        # return rvr==n
        if rvr==n:
            return "it is a palindrome"
    return "not  a plindrome"     
    
name=input("enter: ")
p=palindrome(name)
print(p)
