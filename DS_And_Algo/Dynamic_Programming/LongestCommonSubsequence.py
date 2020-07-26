
#############################################################
# Longest common Subsequence (finally working)
#############################################################

def func():

    X = ['a','g','t','t','b']
    Y = ['a','a','t','t','b','b']

    L = [[0]*(len(Y) + 1) for i in range(len(X) + 1)] 
    # print(len(X))
    # print(len(Y))
    for i in range(len(X)):
        # print('i-',i)
        for j in range(len(Y)):
            if i == 0 and j == 0 :
                L[i][j] = 0
            elif X[i] == Y[j]: 
                L[i+1][j+1] = L[i][j]+1
            else: 
                # print('i',i,'j',j)
                L[i+1][j+1] = max( L[i][j+1], L[i+1][j] )
    print(L[len(X)][len(Y)])
    print(L)

func()