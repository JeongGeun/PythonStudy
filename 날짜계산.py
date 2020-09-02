
dp=[0]*10001

x,a,b,c,d=map(int,input.split())

arr=[1,5,10,25]

for i in range(x+1):
    for j in arr:
        if i+j<=x:
            dp[i+j]=min(dp[i+j],dp[i]+1)

