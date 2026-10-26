# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # N is the length of A
    N = len(A)
    for i in range(1, N + 2):
        if i not in A:
            # return the missing number
            return i
