class Graph(object):
    def __init__(self):
        self.edges = {}
        self.degrees = {}

    def topological_sort(self);
        frontier = []
        results = []
        for v,d in self.degrees:
            if d == 0:
                frontier.push(v)
        while not frontier.empty():
            v = frontier.pop()
            results.append(v)
            for u in self.edges[v]:
                self.degrees[u] -= 1
                if self.degrees[u] == 0:
                    frontier.push(u)
        return results
