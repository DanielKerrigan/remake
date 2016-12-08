from graph import Graph
from collections import deque
import os


class Makefile(object):
    def __init__(self, file_name, start_target, just_print=False):
        self.file_name = file_name
        self.start_target = start_target
        self.graph = Graph()
        # map from target to sources
        self.sources = {}
        # map from target to commands run by that target
        self.actions = {}
        # map from $(variable name) to variable value
        self.variables = {}
        self.just_print = just_print
        # store the output for testing
        self.output = []

    def substitute_variables(self, cmd):
        cmd = [self.variables.get(w, w) for w in cmd.split()]
        return cmd

    def run_makefile(self):
        self.parse_makefile()
        self.build_graph()
        results = self.graph.topological_sort()

        for result in results:
            if result in self.actions:
                commands = self.actions[result]
                for cmd in commands:
                    print(cmd)
                    self.output.append(cmd)
                    if not self.just_print:
                        os.system(cmd)

    # build graph that reverses targets/sources. compute degrees.
    # perform BFS starting from the starting target
    def build_graph(self):
        marked = set()
        frontier = deque()
        frontier.append(self.start_target)
        while frontier:
            t = frontier.popleft()
            if t in marked or t not in self.sources:
                continue
            marked.add(t)

            # update the degrees and edges for the target
            if t in self.graph.degrees:
                self.graph.degrees[t] += len(self.sources[t])
            else:
                self.graph.degrees[t] = len(self.sources[t])

            if t not in self.graph.edges:
                self.graph.edges[t] = []

            # updates degrees and edges for the sources
            for src in self.sources[t]:
                if src not in self.graph.degrees:
                    self.graph.degrees[src] = 0
                if src not in self.graph.edges:
                    self.graph.edges[src] = [t]
                else:
                    self.graph.edges[src].append(t)

            for u in self.sources[t]:
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
            if not self.start_target:
                self.start_target = target

            # sources are after the :
            srcs = self.substitute_variables(line[1].strip('\t'))
            self.sources[target] = srcs

            # places commands in actions dictionary with target as key
            if target not in self.actions:
                self.actions[target] = []
            while line_num < length and '\t' in lines[line_num]:
                # trim whitespace
                cmd = lines[line_num].strip(' \t')
                if cmd:
                    # substitute variables for their values
                    cmd = self.substitute_variables(cmd)
                    cmd = ' '.join(cmd)
                    self.actions[target].append(cmd)
                line_num += 1
