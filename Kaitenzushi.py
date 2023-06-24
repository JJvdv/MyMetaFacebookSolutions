'''
Meta Careers Coding Puzzles
Level 1 - Katitenzushi solution
'''
from typing import List

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    count = 0
    eaten = {}
    for i in range(N): 
        if not D[i] in eaten or (count - eaten[D[i]]) > K:
            eaten[D[i]] = count
            count += 1
    return count