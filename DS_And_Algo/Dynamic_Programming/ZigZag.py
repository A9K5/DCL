
#############################################################
# Problem Statement for ZigZag
# http://community.topcoder.com/tc?module=ProblemDetail&rd=4493&pm=1259
#############################################################

z = [1, 7, 4, 9, 2, 5 ]
z = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
z = [1,17,10,13,10,16,8]
z = [44]
z = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
z = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]


p =[0]*(len(z)-1)
for i in range(len(z)-1):
    p[i] = z[i]-z[i+1]
print(p)
# # Diff calculation complete

# L = [[0]*len(z) for i in range(len(z))]
L = [0]*len(p)
result = 0
# print('L',L)
for i in range(len(L)):
    if i == 0 :
        # print('Lbw',L)
        L[i]=1
        # print('Lbw',L[])
    elif p[i] > 0 and p[i-1] < 0:
        L[i] = L[i-1] + 1
        result = max(result,L[i])
    elif p[i] < 0 and p[i-1] > 0:
        L[i] = L[i-1] + 1
        result = max(result,L[i])
    else:
        L[i] = L[i-1]
result += 1
print('result',result)
print('L',L)

