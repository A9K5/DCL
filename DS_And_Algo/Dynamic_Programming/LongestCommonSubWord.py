#############################################################
# Longest common subword (finally working)
#############################################################


def func():

    X = ['a','g','t','t','b']
    Y = ['a','a','t','t','b','b']

    L = [[0]*(len(Y) + 1) for i in range(len(X) + 1)] 
    # print(len(X))
    # print(len(Y))
    result=0
    for i in range(len(X)):
        for j in range(len(Y)):
            if i == 0 and j == 0 :
                L[i][j] = 0
            elif X[i] == Y[j]: 
                L[i+1][j+1] = L[i][j]+1
                result = max(result,L[i+1][j+1])
            else:
                L[i+1][j+1]=0

    print(result)   
    for i in range(len(L)):
        print(L[i])

func()