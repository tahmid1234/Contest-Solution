from collections import deque
from collections import defaultdict

n, m = map(int, input().split())
INF = 10 ** 9
visited=defaultdict(int)

g = [[] for _ in range(n + m)] # 0..(n-1) -- rows, n..n+m-1 -- columns

for i in range(n):
    s=input()
    for j,c in enumerate(s):
        j_v=n+j
        if(c=="#"):
            g[i].append(j_v)
            g[j_v].append(i)








q = deque([0])

total_col=0
visited[0]=0
while q:
    u=q.popleft()
    visited[u] = visited[u] + 1

    for v in g[u]:

        if(v==n-1):
            visited[n-1]=visited[u]
            q.clear()
            break
        if(visited[v]==0):
            visited[v]=visited[u]
            q.append(v)


print(-1 if (visited[n-1]==0) else visited[n-1])