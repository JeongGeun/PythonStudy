# 문자열 처리 + 그리디
# 처리시간 포함해야 한다는 것 때문에 시간을 많이 소모했다
# 파이썬에서 부동소수점계산은 답이 틀릴 위험이 많으므로 정수부로 끌어올려 계산했다
# 문제의 핵심은 결국 처리량이 변하는 부분은 각 로그의 시작과 끝이다
# 따라서 오름차순으로 정렬된 [시작,끝]값을 가지고 1초씩 더해가며 그 구간 안에 다른 로그들이 속해 있는 지 판단
# 처리시간은 시작값과 끝값을 포함함으로 [A,A+1)로 표현되고 한 구간의 시작이 다른 구간의 끝보다 앞서거나 한 구간의 끝이 다른 구간의 앞보다 뒤에 있으면
# 겹치지 않으므로 이 두가지 경우를 제외한 나머지 경우의 갯수를 세어 MAX값을 구한다.
def solution(lines):
    answer = 0
    sflist=[]
    for line in lines:
        arr = line.split(' ')
        time = arr[1].split(":")
        hour = int(time[0])*3600
        min = int(time[1])*60
        sec =float(time[2])
        duration =float(arr[2][:-1])
        end=(hour + min +sec)*1000
        start = end-(duration*1000)+1
        sflist.append([start,end])

    for i,v in enumerate(sflist):
        cnt=1
        for j,jv in enumerate(sflist):
            if i!=j:
                if not (v[0]+1000<=jv[0] or jv[1]<v[0]):
                    cnt+=1
        answer = max(answer, cnt)
        cnt=1
        for j,jv in enumerate(sflist):
            if i!=j:
                if not (v[1]+1000<=jv[0] or jv[1]<v[1]):
                    cnt+=1
        answer=max(answer,cnt)

    return answer

solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])