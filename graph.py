class Graph(object):
    def __init__(self):
        self.edges = {}
        self.degrees = {}

    def topological_sort(self):
        frontier = []
        results = []
        for v,d in self.degrees.iteritems():
            if d == 0:
                frontier.append(v)
        while frontier:
            v = frontier.pop(0)
            results.append(v)
            
            for u in self.edges[v]:
                self.degrees[u] -= 1
                if self.degrees[u] == 0:
                    frontier.append(u)
        return results
