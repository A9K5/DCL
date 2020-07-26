#######################################
# Fibonacci Series with memo
#######################################

global count 
count=0

def func (n,memo):
    global count
    count+=1
    if memo[n]!=-1:
        return memo[n]
    memo[n] = func(n-1,memo)+func(n-2,memo)
    return memo[n]

memo=[-1]*7  # n+1 size of memo array
memo[0]=0
memo[1]=1
# print(memo)
print(func(5,memo))
# func(n,memo)
print(count)