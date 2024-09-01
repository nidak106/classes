# to showcase the verifying users 
unconfirmed_users=[]
for i in range(3):
    users=input("enter three users: ")
    i=unconfirmed_users.append(users)
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"verifying  user {current_user}")
    confirmed_users.append(current_user)
    
print(f"the following users have been confirmed: ")
for i in confirmed_users:
    print(i)
    
    
    