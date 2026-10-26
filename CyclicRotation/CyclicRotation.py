# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # if is empty then do nothing, just directly return A
    if len(A) == 0:
        return A
    # rotate A K times
    for i in range(K):
        x = A.pop()
        A.insert(0, x)
    return A
