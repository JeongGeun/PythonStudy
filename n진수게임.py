alpha =['A','B','C','D','E','F']

def makeNjinsu(n,num):
    lst=[]
    while num>0:
        rem=num%n
        num=int(num/n)
        if rem>=10:
            lst.append(alpha[rem-10])
        else:
            lst.append(str(rem))
    lst.reverse()
    return "".join(lst)

def solution(n, t, m, p):
    answer = ''
    tcnt=0
    p-=1
    string="0"
    num=1

    while True:
        if tcnt>=t:
            break
        if len(string)>p:
            answer+=string[p]
        else:
            while len(string)<=p:
                string+=makeNjinsu(n,num)
                num+=1
            answer += string[p]
        p+=m
        tcnt+=1
    print(answer)
    return answer

solution(2,4,2,1)
solution(16,16,2,1)
solution(16,16,2,2)