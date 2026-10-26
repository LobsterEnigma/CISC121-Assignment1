# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # count length of A and store in N
    N = len(A)
    for i in range(1, N + 1):
        if i not in A:
            # it's not a permutation
            return 0
    # is a permutation
    return 1
