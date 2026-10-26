# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    
    # u start from 0, then by using u + 1 and count the total number
    u = 0
    # it will be stop when X > Y
    while X < Y:
        X = X + D
        u = u + 1
    else:
        return u
