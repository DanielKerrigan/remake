import unittest
from graph import Graph

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

