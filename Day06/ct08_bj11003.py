# 백준 11003 최솟값 찾기1
from collections import deque

N, L = map(int, input().split()) # 12, 3
mydeque = deque()
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6

# 새 값이 들어올 때 마다 정렬 대신 현재 수 보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재 값보다 크면
        mydeque.pop() # 빼버린다
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L : # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ') # 무조건 최솟값(min()과 동일)
    