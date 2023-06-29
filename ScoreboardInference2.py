from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    count = max(S)
  
    if count % 3 == 0:
        if any(x % 3 != 0 for x in S):
            return count // 3 + 1
  
    if count % 3 == 1 and 1 not in S and count - 1 not in S:
        return count // 3 + 1
  
    return count // 3 + int(any(x % 3 == 1 for x in S)) + int(any(x % 3 == 2 for x in S))