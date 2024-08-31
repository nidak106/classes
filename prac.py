def palindrome(a):
    right=len(a)-1
    left=0
    while right>=left:
        if not a[right]==a[left]:
            return False
        left+=1
        right-=1
    return True    
n=palindrome("afan")
print(n)
        
        