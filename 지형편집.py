
def cal(mid,p,q):
    answer=0
    for i in h:
        if i>=s[mid]:
            answer+=q*(i-s[mid])
        else:
            answer+=p*(s[mid]-i)
    return answer


def solution(land, P, Q):
    answer = 0
    global h
    global s
    h=[]
    s=set()
    n=len(land)
    for i in land:
        for j in i:
            s.add(j)
            h.append(j)
    s=list(s)
    s.sort()
    left=0
    right=len(s)-1
    while left<right:
        mid =(left+right)//2

        m=cal(mid,P,Q)
        m2=cal(mid+1,P,Q)
        
    return answer
