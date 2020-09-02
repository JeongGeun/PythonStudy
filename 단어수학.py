import operator

num = int(input())
arr=[]
visit=[-1]*26

for i in range(num):
    string = input()
    arr.append(string)
que={}

for i in arr:
    for key,val in enumerate(reversed(i)):
        if val in que.keys():
            que[val]+=(10**key)
        else:
            que[val] = (10 ** key)

que =sorted(que.items(),key=operator.itemgetter(1),reverse=True)
start=9
for i,val in que:
    visit[ord(i)-ord('A')]=start
    start-=1

answer=[]
for i in arr:
    num=""
    for val in i:
        num+=str(visit[ord(val)-ord('A')])
    answer.append(int(num))
print(sum(answer))





