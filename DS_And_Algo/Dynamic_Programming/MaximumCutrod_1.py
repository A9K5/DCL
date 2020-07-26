#############################################################
# Maximum cutrod problem. (Recursive problem)
#############################################################

import sys
sys.setrecursionlimit(1500)

p = [1,5,8,9,10,17,17,20,24,30]
n = 5

def func(n):
    q=0
    if n==0:
        return 0
    for i in range(1,n+1):
        q = max( q , p[i-1] + func(n-i) )
    return q

print(func(n))