# 조합 관련 문제
# python은 itertools를 사용해 combinations(list,count)함수를 통해 조합튜플을 구해낸다.
# 조합된 컬럼을 가지고 유일성 만족하는 지 이중 포문으로 확인한다.
# ans list에 만약 최소성을 만족하는 조합이 이미 있을 경우 그 값은 제외한다.

import itertools
def check(relation,item):
    for i in range(0,len(relation)):
        for j in range(0,len(relation)):
            if i<j:
                flag = True
                for k in item:
                    if relation[i][k]!=relation[j][k]:
                        flag=False
                if flag ==True:
                    return False
    return True

def solution(relation):
    answer = 0
    ans=[]
    N=len(relation[0])
    candi =[str(i) for i in range(0,N)]
    for i in range(1,N+1):
        v= list(itertools.combinations(candi,i))
        for sv in v:
            string =''.join(sv)
            flag=True
            cnt=0
            for text in ans:
               for t in text:
                    for s in string:
                        if t==s:
                            cnt+=1
               if len(text)==cnt:
                    flag=False
               cnt=0
            sv=list(map(int,sv))
            if check(relation,sv)==True and flag==True:
                ans.append(sv)
    answer=len(ans)
    return answer
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])