# 백준 1253 좋다
import sys
input  = sys.stdin.readline

N = int(input())
count = 0
A = list(map(int, input().split())) # 입력을 한줄에 다받을때
A.sort() # 전체 정렬

for k in range(N):
    find = A[k]
    i = 0 # i는 리스트 첫번째
    j = N-1 # j는 리스트 마지막번째 위치

    while i < j: # 두 인덱스가 결국 만나면 While문 종료
        if A[i] + A[j] == find: # 두 수의 합이 찾는 수랑 일치
            if i  != k and j != k: # i,j는 k와 같은 위치가 되면 안됨!
                count += 1 
                break
            elif i == k: i += 1 
            elif j == k: j -= 1 
        elif A[i] + A[j] < find: # 두 수의 합이 찾는 수보다 작음
            i += 1  # i를 증가시켜야 합산수가 커짐
        elif A[i] + A[j] > find: # 두 수의 합이 찾는 수보다 큼(else를 써도 무방)
            j -= 1  # j를 감소시켜야 합산수가 작아짐
            
print(count)