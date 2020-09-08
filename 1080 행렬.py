# 그리디 문제
# 각 좌표를 조사하며 정답과 다른 좌표가 있다면 바꾼다
# 왜냐하면 정답과 다른 좌표를 바꿀 수 있는 기회는 그 좌푤를 조사할 때 1번이기 때문이다.

n,m=map(int,input().split())
arr1=[]
arr2=[]
answer=0
def cal(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            if arr1[i][j]=='0':
                arr1[i][j]='1'
            else:
                arr1[i][j]='0'
    return


for i in range(n):
    line=input()
    line =[char for char in line]
    arr1.append(line)

for i in range(n):
    line=input()
    line = [char for char in line]
    arr2.append(line)

for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j]!=arr2[i][j]:
            cal(i,j)
            answer+=1
if arr1==arr2:
    print(answer)
else:
    print(-1)