from graph import Graph
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
        
        #print(results)
        for result in results:
            if result in self.actions:
                commands = self.actions[result]
                for cmd in commands:
                    print(cmd)
                    os.system(cmd)
    
    def build_graph(self):
        path = [self.tg]
        for t in path:
            if t in self.targets:
                sources = self.targets[t]
                # update the degrees dictionary for the target
                if t in self.graph.degrees:
                    self.graph.degrees[t] += len(sources)
                else:
                    self.graph.degrees[t] = len(sources)
               
                if t not in self.graph.edges:
                    self.graph.edges[t] = []
 
                # updates path, and  degrees and edges dictionaries for sources
                for src in sources:
                    if src not in path:
                        path.append(src)
                    if src not in self.graph.degrees:
                        self.graph.degrees[src] = 0
                    if src not in self.graph.edges:
                        self.graph.edges[src] = [t]
                    else:
                        self.graph.edges[src].append(target)
      
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

            line[1] = line[1].strip('\t')
            # sources are the variables after the :
            sources = line[1].split()
            self.targets[target] = sources

            # places commands in actions dictionary with target as key
            if target not in self.actions:
                self.actions[target] = []
            while line_num < length and '\t' in lines[line_num]:
                cmd = lines[line_num].split('#')[0]
                cmd = cmd.strip(' \t')
                if cmd:
                    # substitute variables for their values
                    cmd = [self.variables.get(w, w) for w in cmd.split()]
                    cmd = ' '.join(cmd)
                    self.actions[target].append(cmd)
                line_num += 1
