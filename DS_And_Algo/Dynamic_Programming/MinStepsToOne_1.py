##############################
# Min steps to one
##############################
n = 12
global memo
memo = [-1]*(n+2)

def func(n):
    global memo
    if n==1:
        return 0
    count = 1 + func(n-1)    
    if n%2==0:
        count = 1 + min(count,func(n//2))
    if n%3==0:
        count = 1 + min(count,func(n//3))
    memo[n] = count
    # count = 1 + min(func(n-1),func(n//2),func(n//3))
    return count

print(func(n))
print(memo)