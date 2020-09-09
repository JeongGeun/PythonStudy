# 문자열 처리문제
# 뒤에 # 붙은 것을 해결하려고 굉장히 고생이 많았다
# 다른 풀이를 보니 A#=> H 로 replace해서 푸는 걸 봤는데 굉장히 좋은 방식이다
# 내 코드는 일단 반복할 문자열길이에서 #의 갯수를 빼준다음 몫을 곱하고
# while문 돌려서 나머지 만큼 더해주는 게 포인트다.
# 마지막에 return none때문에 어이없이 시간을 날렸다. -> 담부터는 1시간이 넘도록 못 풀 경우 해설을 보는 걸 추천한다.

def solution(m, musicinfos):
    answer = ''
    sharp =['A','C','D','F','G']
    maxtime =0
    for s in musicinfos:
        arr=s.split(",")
        stime=arr[0].split(":")
        etime=arr[1].split(":")
        smin =int(stime[0])*60+int(stime[1])
        emin =int(etime[0])*60+int(etime[1])
        dif =emin-smin
        sharpcnt=arr[3].count("#")
        a = dif//(len(arr[3])-sharpcnt)
        b = dif %(len(arr[3])-sharpcnt)
        scnt=0
        narr= arr[3]*a
        for i in range(len(arr[3])):
            if arr[3][i]=="#":
                continue
            if scnt == b:
                break
            if arr[3][i] in sharp:
                if i+1<len(arr[3]):
                    if arr[3][i+1]=="#":
                        narr+=arr[3][i:i+2]
                        scnt+=1
                        continue
            narr+=arr[3][i]
            scnt+=1
        for i in range(len(narr)):
            if i+len(m)>len(narr):
                break
            if narr[i:i+len(m)]==m:
                if i+len(m)<len(narr):
                    if narr[i+len(m)]=='#' and m[-1] in sharp:
                        continue
                if maxtime<dif:
                    answer=arr[2]
                    maxtime=dif

    if len(answer)==0:
        answer="`(None)`"
    return answer

solution("ABC",["12:00,12:14,HELLO,C#DEFGAB","13:00,13:05,WORLD,ABCDEF"])