from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    last = min(P)
    count = N - last
    return count
