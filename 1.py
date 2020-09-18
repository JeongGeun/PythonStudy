def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    lst = [char for char in new_id]
    nlst =[]
    for i in lst:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            nlst.append(i)
    nlst ="".join(nlst)
    print(nlst)
    idx=0
    nans=[]
    while idx<len(nlst):
        if len(nans)==0:
            nans.append(nlst[idx])
        else:
            if nans[-1]=="." and nlst[idx]=='.':
                pass
            else:
                nans.append(nlst[idx])
        idx+=1
    print(nans)
    return answer

solution(	"...!@BaT#*..y.abcdefghijklm")