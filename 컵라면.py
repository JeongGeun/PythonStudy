## 그리디를 이용한 풀이
## 1. 데드라인이 높은 순으로 list를 정렬한다
## 2. 데드라인이 높은 순으로 pq에 넣으면서 각 데드라인마다 pq.top을 뽑아 answer에 더한다.
## tips : python은 lambda를 통해 sorting기준을 정하는데 key=lambda x: 조건 이런 방식이다.
## 우선순위 q는 PriorityQueue()

import sys
from queue import PriorityQueue

num =int(sys.stdin.readline())
ans=0
arrlist=[]
q=PriorityQueue()

for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    arrlist.append([a,b])
arrlist=sorted(arrlist,key=lambda x:-x[0])
idx=0
for i in range(num,0,-1):
    while idx<num:
        if arrlist[idx][0]!=i:
            break
        else:
            q.put([-arrlist[idx][1],arrlist[idx][0]])
        idx+=1
    if q.empty()==False:
        ans-=q.get()[0]
print(ans)




