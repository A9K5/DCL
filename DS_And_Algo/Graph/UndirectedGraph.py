# Undirected Graph Stored in the form of adjacency list
from collections import defaultdict

g = defaultdict(list)
comp = []
N = int(input())
used = [False for i in range(N+1)]
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    g[a].append(b)
    g[b].append(a)
print(g)

"""
5
5
1 2
2 3
3 4
4 5
3 5
defaultdict(<class 'list'>, 
{
    1: [2], 
    2: [1, 3], 
    3: [2, 4, 5], 
    4: [3, 5], 
    5: [4, 3]
}   )
"""