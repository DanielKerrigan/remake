from graph import Graph

class Makefile(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.graph = Graph()
        self.actions = {}        

    def parse_makefile(self):
        # only handles dependencies for now
        lines = self.file_name.read().splitlines()
        # enumerate returns a tuple with the index as well as the content
        for line_num, line in enumerate(lines):
            if line.find(':') == -1:
                continue
            line = line.split(':')
            #LEFT OFF HERE
            # get rid of tabs and split a line into a list of vertices
            # compilation line right after
            actions[line[0]] = lines[line_num + 1]
        
