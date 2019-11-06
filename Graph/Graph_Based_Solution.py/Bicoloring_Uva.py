#https://onlinejudge.org/external/100/10004.pdf

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self, source, dest):
        self.graph[source].append(dest)
        self.graph[dest].append(source)

    def bicoloring(self, source):
        
        queue = []
        color = ['white'] * (len(self.graph) + 1)
        queue.append(source)
        color[source] = 'red'

        while queue:
            
            u = queue.pop(0)

            for v in self.graph[u]:
                if color[v] == 'white':

                    if color[u] == 'red':
                        color[v] = 'blue'
                    else:
                        color[v] = 'red'
                    queue.append(v)
                if color[u] == color[v]:
                    return False
        return True

if __name__ == "__main__":
    while True:
        g = Graph()
        n = int(input())
        if n == 0:
            break
        l = int(input())
        for _ in range(l):
            a, b = map(int, input().split())
            g.addEdges(a, b)

        if g.bicoloring(0):
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
