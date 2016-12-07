from graph import Graph

class Makefile(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.graph = Graph()
        self.actions = {}        

    def parse_makefile(self):
        # only handles dependencies for now
        with open(self.file_name) as f:
          lines = f.read().splitlines()

        # enumerate returns a tuple with the index as well as the content
        for line_num, line in enumerate(lines):
            if line.find(':') == -1:
                continue
            line = line.split(':')
            # target is the variable that preceds the :
            target = line[0]
            line[1] = line[1].strip('\t')
            # sources are the variables after the :
            sources = line[1].split(' ')
          
            # update the degrees dictionary for the target 
            if target in self.graph.degrees:
                self.graph.degrees[target] += len(sources)
            else:
                self.graph.degrees[target] = len(sources)
        
            if target not in self.graph.edges:
                self.graph.edges[target] = []

            # updates degrees and edges dictionaries for sources
            for src in sources:
                if src not in self.graph.degrees:
                    self.graph.degrees[src] = 0
                if src not in self.graph.edges:
                    self.graph.edges[src] = [target]
                else:
                    self.graph.edges[src].append(target)
            
            # places compilation line in actions dictionary with target as key
            self.actions[target] = lines[line_num + 1]
        
