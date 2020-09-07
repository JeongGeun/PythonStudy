# 문자열 처리
# 분기가 중요했던 문제
# 문자열 어디서 끊어야 하는 지에 대한 개념이 헷갈렸다
# SDT에서 리스트에 넣고 *,#인 경우에는 리스트안에 있는 원소 이용

def solution(dartResult):
    answer = 0
    num=''
    score=[]
    for i in dartResult:
        if i.isdigit():
           num+=i
        elif i=='S':
            score.append(int(num))
            num=''
        elif i=='T':
            score.append(int(num)**3)
            num = ''
        elif i=='D':
            score.append(int(num)**2)
            num = ''
        elif i=='*':
            if len(score)>1:
                score[-2]*=2
            score[-1]*=2
        else:
            score[-1]*=-1
    answer=sum(score)
    return answer


solution("1S*2T*3S")