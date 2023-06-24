'''
Meta Careers Coding Puzzles
Level 1 - Scoreboard Inference solution
'''

from typing import List
import math

def getMinProblemCount(N: int, S: List[int]) -> int:
    min = 0;
    for i in range(N):
        print("S[i] = ", S[i])
        print("count = ", min)
        if S[i] / 2 > 0:
            print(math.ceil(S[i] / 2)) # maybe something like if < 1 add 1 else 2??
            min += math.ceil(S[i] / 2)
    print(min)
    return min


if __name__ == "__main__":
    N = 6
    S = [1, 2, 3, 4, 5, 6]

    #N = 4
    #S = [4, 3, 3, 4]

    #N = 4
    #S = [2, 4, 6, 8]

    getMinProblemCount(N, S)