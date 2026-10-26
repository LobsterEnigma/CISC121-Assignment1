# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A): 
    for x in A:
        # if x is odd number, then no pair
        if A.count(x) % 2 == 1:
            return x
