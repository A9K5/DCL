#############################################################
# Maximum cutrod problem . (bottom up approach )
#############################################################

import sys
sys.setrecursionlimit(1500)

p = [1,5,8,9,10,17,17,20,24,30]
n = 9
r = [0]*(n+1)

def func(n): 
    r = [0]*(n+1)
    for j in range(1,n+1):
        q=-1
        for i in range(1,j+1):
            q = max( q , p[i-1] + r[j-i] )
        r[j]=q 
    print(r[n])
    return r

print(func(n))