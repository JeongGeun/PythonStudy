num =int(input())
dp=[1e9]*5001
arr=[3,5]
dp[num]=0
for i in arr:
    for j in range(num,0,-1):
        if j-i>=0:
            dp[j-i]=min(dp[j]+1,dp[j-i])
if dp[0]==1e9:
    dp[0]=-1
print(dp[0])