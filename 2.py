from itertools import combinations
from collections import defaultdict

# 각각의 course값마다 조합을 뽑아주고 비트마스크를 응용하여 각 조합에 인덱스를 부여한다
# 그 후 max값을 찾은 뒤 max값을 가지는 index를 뽑은 다음 그 index를 비트이전형태로 돌린다.
# index를 answer에 담고 모든 index값이 담기면 answer를 sorting하여 리턴한다.

def solution(orders, course):
    answer = []
    for n in course:
        vec=defaultdict(int)
        for text in orders:
            text=[char for char in text]
            com= list(combinations(text,n))
            for i in com:
                num = 0
                for j in i:
                    num=num+2**(ord(j)-ord('A'))
                vec[num]+=1
        ma=1
        for key,val in vec.items():
            if val>ma:
                ma=val
        for key,val in vec.items():
            if ma==val:
                lst=""
                nnum= key
                idx=0
                while nnum>0:
                    cnt=nnum%2
                    if cnt==1:
                        lst= lst + chr(ord("A")+idx)
                    nnum=nnum//2
                    idx+=1
                answer.append(lst)
    answer.sort()
    print(answer)
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])