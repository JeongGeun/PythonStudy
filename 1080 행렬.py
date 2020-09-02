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