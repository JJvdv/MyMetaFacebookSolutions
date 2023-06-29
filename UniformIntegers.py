def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    count = 0
    max_length = len(str(B))
    for length in range(1, max_length + 1):
        count += sameDigits(length, A, B)
    return count

def sameDigits(length: int, A: int, B: int) -> int:
    count = 0

    for digit in range(10):
        num = int(str(digit) * length)
        if num >= A and num <= B:
            count += 1

    return count