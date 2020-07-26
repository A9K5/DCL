#############################################################
# Problem Statement for BadNeighbors (Memoization)
############################################################# 


z = [10, 3, 2, 5, 7, 8]
# z = [11, 15 ]
# z = [7, 7, 7, 7, 7, 7, 7]
z = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
z = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]


def func(z):
    if len(z) < 3:
        return max(z)
    else:
        result = [-1]*len(z)
        result[0] = z[0]
        result[1] = z[1]
        result[2] = z[0] + z[2]
        for i in range( 3 , len(z) ):
            result[i] = z[i] + max(result[:i-1])
        return result[-1]

print( max ( func(z[1:]) , func(z[:-1]) ) )
