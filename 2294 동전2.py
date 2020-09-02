
n,k=map(int,input().split())
arr=[]
dp=[1e9]*10001
for i in range(n):
    num =int(input())
    arr.append(num)
dp[0]=0
for i in arr:
    for j in range(k+1):
        if i+j<=k:
            dp[i+j]=min(dp[i+j],dp[j]+1)
if dp[k]==1e9:
    dp[k]=-1
print(dp[k])
