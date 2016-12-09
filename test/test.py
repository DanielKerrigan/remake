import unittest
import os
from graph import Graph
from makefile import Makefile


class TestTopologicalSort(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

        self.graph.edges = {
            'library.c': ['library.o'],
            'library.h': ['library.o', 'main.o'],
            'main.c': ['main.o'],
            'library.o': ['program'],
            'main.o': ['program'],
            'program': []
        }

        self.graph.degrees = {
            'library.c': 0,
            'library.h': 0,
            'main.c': 0,
            'library.o': 2,
            'main.o': 2,
            'program': 2
        }

    def test_sort(self):
        results = self.graph.topological_sort()
        correct = ['library.c', 'main.c', 'library.h',
                   'library.o', 'main.o', 'program']
        self.assertEqual(results, correct)

    def test_cycle(self):
        # add cycle to the graph
        self.graph.edges['main.o'].append('main.c')
        self.graph.degrees['main.c'] += 1
        with self.assertRaises(RuntimeError):
            self.graph.topological_sort()


class TestMakefile1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.chdir('test/test_1')

    @classmethod
    def tearDownClass(self):
        # returns to original directory after tests are run
        os.chdir('../../')

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

    def test_cycle(self):
        mf = Makefile('Makefile', 'cycle', True)
        # sys.exit should be called
        with self.assertRaises(SystemExit):
            mf.run_makefile()


class TestMakeFile2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir('test/test_2')

    @classmethod
    def tearDownClass(self):
        # returns to original directory after tests are run
        os.chdir('../../')

    def tearDown(self):
        # removes files left after a method e.x. test_output_make_make
        mf = Makefile('Makefile', 'clean', False)
        mf.run_makefile()

    def test_output_make_all(self):
        mf = Makefile('Makefile', '', True)
        mf.run_makefile()
        correct = ['gcc -std=gnu99 -Wall -c -o hello.o hello.c',
                   'gcc -std=gnu99 -Wall -c -o main.o main.c',
                   'gcc -o hello main.o hello.o']
        self.assertEqual(mf.output, correct)

    def test_output_make_clean(self):
        mf = Makefile('Makefile', 'clean', True)
        mf.run_makefile()
        correct = ['rm -f hello *.o']
        self.assertEqual(mf.output, correct)

    # checks that unchanged files are not recompiled
    def test_output_make_make(self):
        # mf needs to set just_print to false in order to test mf2
        mf = Makefile('Makefile', '', False)
        mf.run_makefile()
        mf2 = Makefile('Makefile', '', True)
        mf2.run_makefile()
        correct = []
        self.assertEqual(mf2.output, correct)

    # checks that changed files are recompiled
    def test_output_make_clean_make(self):
        mf = Makefile('Makefile', '', False)
        mf.run_makefile()
        mf2 = Makefile('Makefile', 'clean', False)
        mf2.run_makefile()
        mf3 = Makefile('Makefile', '', True)
        mf3.run_makefile()
        correct = ['gcc -std=gnu99 -Wall -c -o hello.o hello.c',
                   'gcc -std=gnu99 -Wall -c -o main.o main.c',
                   'gcc -o hello main.o hello.o']
        self.assertEqual(mf3.output, correct)
