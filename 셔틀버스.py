# 구현문제
# 마지막 시간대에 집중해서 마지막 버스에 남는 자리가 있으면 답은 무조건 마지막 시간대의 버스를 탄다
# 만약 마지막 시간대의 버스에 남는 자리가 없으면 제일 나중 시간의 사람보다 -1한 시간을 넣는다.

from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    timelst=[]
    for i in timetable:
        time = i.split(":")
        timelst.append(int(time[0])*60+int(time[1]))
    timelst=sorted(timelst)
    timelst=deque(timelst)
    start =9*60
    end =start+n*t
    while start<end:
        temp=[]
        for j in range(m):
            if len(timelst)>0:
                if timelst[0]<=start:
                    temp.append(timelst.popleft())
        if start==end-t:
            if len(temp)==0:
                answer=start
            elif len(temp)==m:
                answer=temp[-1]-1
            else:
                answer=start
        start += t
    hour =answer//60
    min = answer%60
    if hour<10:
        hour ="0" +str(hour)
    else:
        hour = str(hour)

    if min<10:
        min ="0"+str(min)
    else:
        min=str(min)
    return hour+":"+min