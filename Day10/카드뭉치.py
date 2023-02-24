from collections import deque

def solution1(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for item in goal:
        if cards1 and item == cards1[0]:
            cards1.popleft()
        elif cards2 and item == cards2[0]:
            cards2.popleft()
        else: return 'No'
    
    return 'Yes'

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
        
print(solution1(cards1, cards2, goal))

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution1(cards1, cards2, goal))