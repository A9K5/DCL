# https://cp-algorithms.com/graph/search-for-connected-components.html

from collections import defaultdict
def dfs(v):
    global used,g,comp
    used[v] = True
    comp.append(v)
    for i in g[v]:
        if used[i] == False:
            dfs(i)

def fincomps():
    global used,g,comp,N
    for i in g:
        if used[i]==False:
            comp = []
            dfs(i)
            print("components:")
            print(*comp)


g = defaultdict(list)
comp = []
N = int(input())
used = [False for i in range(N+1)]
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    g[a].append(b)
    g[b].append(a)
fincomps()

"""
5
5
1 2
2 3
3 4
4 5
3 5
components:
1 2 3 4 5

5
3
1 5
1 2
3 4
components:
1 5 2
components:
3 4

"""