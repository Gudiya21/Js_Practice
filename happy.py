user=int(input("enter number"))
while user>9:
    digit=0
    sum=0
    while user!=0:
        digit=user%10
        sum+=digit**2
        user//=10
    user=sum
if sum==1:
    print("Happy Number")
else:
    print("Not happy Number")