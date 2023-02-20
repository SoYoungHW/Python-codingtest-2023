# 백준 10989 수 정렬하기3
# 정렬 문제를 풀 때 이 코드를 외워두면 좋을것 같다.(음수가없는경우에)
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for i in range(N): # 천만번
    count[int(input())] += 1 

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)