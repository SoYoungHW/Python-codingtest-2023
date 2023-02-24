def solution2(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)
    
    for i in new_reserve:
        if i-1 in new_lost: new_lost.remove(i-1)
        elif i+1 in new_lost: new_lost.remove(i+1)
    
    return n-len(new_lost)

n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution2(n, lost, reserve)) # return 5

n = 5
lost = [2, 4]
reserve = [3]

print(solution2(n, lost, reserve)) # return 4

n = 3
lost = [3]
reserve = [1]

print(solution2(n, lost, reserve)) # return 2