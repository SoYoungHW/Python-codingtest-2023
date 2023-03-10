# 백준 1753 최단경로
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
mylist = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 가중치 w 엣지
    mylist[u].append((v, w))

q.put((0, K)) # 시작점K queue 넣을때는 가중치, 노드순
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1] # 노드
    if visited[c_v]: continue

    visited[c_v] = True
    for tmp in mylist[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next)) # 가중치로 오름차순

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else: print('INF')