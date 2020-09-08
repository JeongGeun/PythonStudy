# dp
# 동전1과 유사한데 이번에는 k를 최소한의 동전만 사용해서 만들어야 한다
# dp를 무한으로 set하고 dp[0]=0으로 세팅한 후 동전 값만큼 인덱스에 더해가면서 동전 갯수를 센다.
# dp[i+j]=min(dp[j]+1,dp[i+j])의 점화식을 통해
# dp[k]의 값을 도출한다.


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
