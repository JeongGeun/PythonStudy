
n, k = map(int,input().split())
arr=[]
for i in range(n):
    num =int(input())
    arr.append(num)
dp=[0]*10001
dp[0]=1
for i in arr:
    for j in range(k+1):
        if j+i<=k:
            dp[i+j]+=dp[j]
print(dp[k])