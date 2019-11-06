# Problem Link:-https://www.hackerrank.com/challenges/bfsshortreach/problem
# Time O(V + E), Where V is number of  vertices in graph and E is number of Edges in graph.


from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self, source, dest):
        self.graph[source].append(dest)
        self.graph[dest].append(source)

    def BFS(self, source, n):

        queue = []
        queue.append(source)
        distance = defaultdict(int)

        while queue:

            u = queue.pop(0)
            
            for v in self.graph[u]:
                if distance[v] == 0:
                    distance[v] += 6
                    distance[v] += distance[u]
                    queue.append(v)
                    
        return distance
            

def bfs(n, m, edges, s):
    solution = Solution()
    
    for edge in edges:
        solution.addEdges(edge[0], edge[1])
    dist = solution.BFS(s, n+1)

    res = []
    for i in range(1, n+1):
        if i == s:
            continue
        elif dist[i] != 0:
            res.append(dist[i])
        elif dist[i] == 0:
            res.append(-1)

    return res

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        print(' '.join(map(str, result)))
