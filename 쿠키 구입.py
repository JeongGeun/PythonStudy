def solution(cookie):
    answer = 0
    n=len(cookie)
    psum=[0]*(n+1)
    arr=[0]*(n+1)
    for i in range(1,n+1):
        arr[i]=cookie[i-1]
    for i in range(1,n+1):
        psum[i]=psum[i-1]+arr[i]
    for m in range(1,n+1):
        left=1
        right =n
        while True:
            if left>m or right<=m:
                break
            first = psum[m]-psum[left-1]
            second = psum[right]-psum[m]
            if first ==second:
                answer =max(answer,first)
            elif first>second:
                left+=1
            elif second>first:
                right-=1
    return answer