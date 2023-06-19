from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  minSeconds = 0
  pos = 1
  
  for i in range(M):
    targetPos = C[i]
    clockWise = abs(targetPos - pos)
    counterClockWise = N - clockWise
    minSeconds += min(clockWise, counterClockWise)
    pos = targetPos
  return minSeconds