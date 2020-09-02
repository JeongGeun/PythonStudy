T =int(input())
arr=[300,60,10]
ans=[]
for i in arr:
    ans.append(T//i)
    T=T%i
if T!=0:
    print(-1)
else:
    ans=list(map(str,ans))
    answer =" ".join(ans)
    print (str(answer))



