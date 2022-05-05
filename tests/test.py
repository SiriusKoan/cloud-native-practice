import unittest
from funcs import HarryPotter

class Test(unittest.TestCase):
    def setUp(self):
        self.hp = HarryPotter()

    def tearDown(self):
        pass

    def testBasics(self):
        self.assertEqual(0, self.hp.getPrice([]))
        self.assertEqual(8, self.hp.getPrice([1]))
        self.assertEqual(8, self.hp.getPrice([2]))
        self.assertEqual(8, self.hp.getPrice([3]))
        self.assertEqual(8, self.hp.getPrice([4]))
        self.assertEqual(8 * 3, self.hp.getPrice([1, 1, 1]))
