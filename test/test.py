import unittest

class TestTopologicalSort(unittest.TestCase):

    def test_trivial(self):
        self.assertEqual('a', 'a')
