arr=[31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    a,b,c = map(int,input().split())
    ans=0
    arr[1]=28
    if a==0 and b==0 and c==0:
        break
    if c%4==0:
        if c%100!=0:
            arr[1]=29
        else:
            if c%400==0:
                arr[1]=29
    for mon in range(0,b-1):
        ans+=arr[mon]
    ans+=a
    print(ans)




