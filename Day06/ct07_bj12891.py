# 백준 12891 DNA 비밀번호
Checklist = [0] * 4 # ACGT 유전자값
mylist = [0] * 4 # 부분 문자열의 ACGT 갯수
CheckSecret = 0

# 함수정의
def myadd(c): # 새로 들어온 문자를 처리
    global Checklist, mylist, CheckSecret
    if c == 'A':
        mylist[0] += 1 
        if mylist[0] == Checklist[0]:
            CheckSecret += 1
    elif c == 'C':
        mylist[1] += 1 
        if mylist[1] == Checklist[1]:
            CheckSecret += 1 
    elif c == 'G':
        mylist[2] += 1 
        if mylist[2] == Checklist[2]:
            CheckSecret += 1 
    elif c == 'T':
        mylist[3] += 1 
        if mylist[3] == Checklist[3]:
            CheckSecret += 1 

def myremove(c): # 제거되는 문자를 처리
    global Checklist, mylist, CheckSecret
    if c == 'A':
        if mylist[0] == Checklist[0]:
            CheckSecret -= 1
        mylist[0] -= 1 
    elif c == 'C':
        if mylist[1] == Checklist[1]:
            CheckSecret -= 1 
        mylist[1] -= 1 
    elif c == 'G':
        if mylist[2] == Checklist[2]:
            CheckSecret -= 1 
        mylist[2] -= 1 
    elif c == 'T':
        if mylist[3] == Checklist[3]:
            CheckSecret -= 1 
        mylist[3] -= 1

S, P = map(int, input().split())
result = 0
A = list(input())
Checklist = list(map(int, input().split()))

# print(S, P)
# print(result)
# print(A)
# print(Checklist)

for i in range(4):
    if Checklist[i] == 0: # ACGT 4
        CheckSecret += 1  # 0 없어도 되니까 처음부터 4로 맞추기위한 초기화

for i in range(P): # 부분 문자열 갯수만큼 2 
    myadd(A[i])

if CheckSecret == 4: # ACGT # 4는 네자리 유전자 글자 다 조건만족
    result += 1

for i in range(P, S): # 2, 4
    j = i - P # 0 - 2 = -2
    myadd(A[i]) # 이번 슬라이드에서 처리된 값을 추가
    myremove(A[j]) # 이전 슬라이드에서 처리한 값을 제거
    if CheckSecret == 4:
        result += 1 

print(result)