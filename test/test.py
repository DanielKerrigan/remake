import unittest
import os
from graph import Graph
from makefile import Makefile


class TestTopologicalSort(unittest.TestCase):

    def test_sort(self):
        graph = Graph()

        graph.edges = {
            'library.c': ['library.o'],
            'library.h': ['library.o', 'main.o'],
            'main.c': ['main.o'],
            'library.o': ['program'],
            'main.o': ['program'],
            'program': []
        }

        graph.degrees = {
            'library.c': 0,
            'library.h': 0,
            'main.c': 0,
            'library.o': 2,
            'main.o': 2,
            'program': 2
        }

        results = graph.topological_sort()
        correct = ['library.c', 'main.c', 'library.h',
                   'library.o', 'main.o', 'program']
        self.assertEqual(results, correct)


class TestMakefile(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        os.chdir('test/test_1')

    def test_output_make_all(self):
        mf = Makefile('Makefile', '', True)
        mf.run_makefile()
        correct = ['g++ solution.cpp -g -Wall -std=gnu++11 -o solution',
                   'touch test.xyz']
        self.assertEqual(mf.output, correct)

    def test_output_make_clean(self):
        mf = Makefile('Makefile', 'clean', True)
        mf.run_makefile()
        correct = ['rm solution test.xyz']
        self.assertEqual(mf.output, correct)

    def test_output_make_solution_cpp(self):
        mf = Makefile('Makefile', 'solution', True)
        mf.run_makefile()
        correct = ['g++ solution.cpp -g -Wall -std=gnu++11 -o solution',
                   'touch test.xyz']
        self.assertEqual(mf.output, correct)
