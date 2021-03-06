from collections import deque


class Graph(object):
    def __init__(self):
        self.edges = {}
        self.degrees = {}

    def topological_sort(self):
        frontier = deque()
        results = []
        for v, d in self.degrees.iteritems():
            if d == 0:
                frontier.append(v)
        while frontier:
            v = frontier.popleft()
            results.append(v)

            for u in self.edges[v]:
                self.degrees[u] -= 1
                if self.degrees[u] == 0:
                    frontier.append(u)

        if len(results) < len(self.degrees):
            raise RuntimeError('Graph has cycles.')

        return results
