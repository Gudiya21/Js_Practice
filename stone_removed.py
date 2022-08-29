arr=[(0,0),(0,1),(1,1),(1,0)]
for i in range(len(arr)-1):
    if arr[i][0]==arr[i][1]:
        arr.remove(arr[i])
print(arr)