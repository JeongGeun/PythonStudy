# dp
# 그리디일 것 같은 문제지만 dp다
# 쓸 수 있는 동전의 값을 입력받고 0부터 k끼지 입력받은 동전 값을 더해가며 k값에 다다르는 dp[k]값을 도출해낸다


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