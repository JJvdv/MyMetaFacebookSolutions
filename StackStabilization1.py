from typing import List


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0

  if (R[N - 1] >= N):
    for i in range(N-2, -1, -1):
      if R[i] < R[i + 1]:
        pass
      else:
        if R[i + 1] > 1:
          R[i] = R[i + 1] - 1
          count += 1
        else:
          return -1  
  else:
    return -1
  
  return count