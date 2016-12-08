from graph import Graph
from collections import deque
import os


class Makefile(object):
    def __init__(self, file_name, tg):
        self.file_name = file_name
        self.tg = tg
        self.graph = Graph()
        self.targets = {}
        self.actions = {}
        self.variables = {}

    def run_makefile(self):
        self.parse_makefile()
        self.build_graph()
        results = self.graph.topological_sort()
        
        for result in results:
            if result in self.actions:
                commands = self.actions[result]
                for cmd in commands:
                    print(cmd)
                    os.system(cmd)
    
    # build graph that reverses targets/sources. compute degrees.
    # perform BFS starting from the target passed via command line
    def build_graph(self):
        marked = set()
        frontier = deque()
        frontier.append(self.tg)
        while frontier:
            t = frontier.popleft()
            if t in marked:
                continue
            marked.add(t)

            # update the degrees and edges for the target
            if t in self.graph.degrees:
                self.graph.degrees[t] += len(sources)
            else:
                self.graph.degrees[t] = len(sources)

            if t not in self.graph.edges:
                self.graph.edges[t] = []

            # updates degrees and edges for the sources
            for src in self.targets[t]:
                if src not in self.graph.degrees:
                    self.graph.degrees[src] = 0
                if src not in self.graph.edges:
                    self.graph.edges[src] = [target]
                else:
                    self.graph.edges[src].append(target)

            for u in self.targets[v]:
                frontier.append(u)

    # parse the makefiles to get the targets and their sources
    def parse_makefile(self):
        with open(self.file_name) as f:
            lines = f.read().splitlines()

        line_num = 0
        length = len(lines)
        while line_num < length:
            line = lines[line_num]
            line_num += 1

            # remove comments
            line = line.split('#')[0]
            # parse variable
            if '=' in line:
                line = line.split('=', 1)
                # surround name with dereference operator
                var_name = '$({})'.format(line[0].strip())
                self.variables[var_name] = line[1].strip()
                continue

            if ':' not in line:
                continue

            line = line.split(':')
            # target is the variable that precedes the :
            target = line[0]
            # if no command line target was specified, make default the first
            if not self.tg:
                self.tg = target

            # sources are the variables after the :
            sources = substitute_variables(line[1].strip('\t'))
            self.targets[target] = sources

            # places commands in actions dictionary with target as key
            if target not in self.actions:
                self.actions[target] = []
            while line_num < length and '\t' in lines[line_num]:
                # remove comments and trim whitespace
                cmd = lines[line_num].split('#')[0]
                cmd = cmd.strip(' \t')
                if cmd:
                    # substitute variables for their values
                    cmd = substitute_variables(cmd)
                    cmd = ' '.join(cmd)
                    self.actions[target].append(cmd)
                line_num += 1

    def substitute_variables(cmd):
        cmd = [self.variables.get(w, w) for w in cmd.split()]
        return cmd

