
#############################################################
# Maximum cutrod problem . (top down approach )
#############################################################

import sys
sys.setrecursionlimit(1500)

p = [1,5,8,9,10,17,17,20,24,30]
n = 4
r = [0]*(n+1)

def func(n,r):
    if r[n]>0:
        print('r[n]',r[n],n)
        return r[n]
    if n==0:
        q=0
    else:
        q = 0
        for i in range(1,n+1):
            q = max( q , p[i-1] + func(n-i,r) )
    r[n] = q 
    return q 

print(func(n,r))
print(r)

