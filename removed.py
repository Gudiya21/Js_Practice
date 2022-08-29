list=[0,0,1,1,1,2,2,3,3,4]
i=0  #Intialization
rem=[]  #remove
while i<len(list): #Length
    if list[i] not in rem:  
        rem.append(list[i])
    i+=1
print(rem)