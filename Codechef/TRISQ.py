##############################
# Fit Squares in Triangle Problem Code: TRISQ
##############################

def func(n):
    if n==0 or n==1 :
        return 0
    return ( ( n//2 - 1) + func(n-2) )

for _ in range(int(input())):
    print(func(int(input())))


for _ in range(int(input())):
    b = int(input())
    b //= 2
    b -= 1
    ans = (b*(b+1))//2
    print( ans )