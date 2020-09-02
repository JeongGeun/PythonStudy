
dp=[0]*1001
n=int(input())

arr =list(map(int,input().split()))
arr =[0]+arr
for i in range(0,n+1):
    for j in range(0,n+1):
        if i+j<=n:
            dp[i+j]=max(dp[i]+arr[j],dp[i+j])

print(dp[n])
