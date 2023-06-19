from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  res = 0
  if len(S) != M:
    return 0
  if M == 0:
    return math.ceil(N / (K + 1))
  S.sort()
  res += (math.ceil((S[0] - 1 + 1) / (K + 1)) - 1)
  for i in range(1, len(S)):
    res += (math.ceil((S[i] - S[i - 1] + 1) / (K + 1)) - 2)
  res += (math.ceil((N - S[-1] + 1) / (K + 1)) - 1)
  return res


