# arr = [1,5,7,1]
# 
# for i in range(len(arr)-1):
#     for j in range(i,len(arr)-1):
#         if arr[i] + arr[j+1] == 6:
#             print(arr[i],arr[j+1])


t = int(input())

for _ in range(t):
    a = []
    n,sum = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(len(arr)-1):
        for j in range(i,len(arr)-1):
            if arr[i] + arr[j+1] == sum:
                b = []
                b.append(arr[i])
                b.append(arr[j+1])
                a.append(b)
    print(len(a))
