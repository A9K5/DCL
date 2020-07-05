# Reference : https://cp-algorithms.com/graph/bridge-searching.html

def DFS(u,par):
    global timer,low,inn,visited,graph,count
    # print(u,par)

    visited[u] = 1
    low[u]=inn[u]=timer
    timer += 1

    for i in graph[u]:
        if i == par:
            continue
        if visited[i] == 1: # back edge being checked overe here.
            low[u] = min(low[u],inn[i])
        else:
            DFS(i,u)
            low[u] = min(low[u],low[i])
            if low[i] > inn[u]:
                count += 1
                print(u,"-",i," : is a  bridge.") # Print each bridge .
            


count = 0
timer = 0
from collections import defaultdict
graph = defaultdict(list)

N = int(input())
visited = [0 for _ in range(N+1)]
low = [0 for _ in range(N+1)]
inn = [0 for _ in range(N+1)]

for _ in range(int(input())):
    A,B = list(map(int,input().split()))
    graph[A].append(B)
    graph[B].append(A)

DFS(1,-1)
print("Count of bridges: ",count)
# Print the number of briges in the graph.


"""
5
5
1 2
2 3
3 4
4 5
3 5
2 - 3  : is a  bridge.
1 - 2  : is a  bridge.
Count of bridges:  2

"""