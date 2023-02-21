# 백준 1920 수 찾기
N = int(input())
A = list(map(int, input().split())) # 4 1 5 2 3
A.sort() # 파이썬 리스트에서 제공하는 기본정렬
M = int(input())
targetList = list(map(int, input().split())) # 1 3 7 9

# print(A)

for i in range(M):
    find = False
    target = targetList[i]

    # 이진탐색시작
    start = 0
    end = N - 1
    while start <= end:
        midle = (start+end) // 2 # 중앙 인덱스
        midVal = A[midle] # 중앙에 있는 값
        if midVal > target: # 오른쪽 날림
            end = midle- 1
        elif midVal < target: # 왼쪽 날림
            start = midle + 1
        else: # 값 찾음
            find = True
            break
    if find:
        print(1)
    else:
        print(0)