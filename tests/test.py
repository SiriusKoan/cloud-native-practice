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

    def testSimpleDiscounts(self):
        self.assertEqual(8 * 2 * 0.95, self.hp.getPrice([0, 1]))
        self.assertEqual(8 * 3 * 0.9, self.hp.getPrice([0, 2, 4]))
        self.assertEqual(8 * 4 * 0.8, self.hp.getPrice([0, 1, 2, 4]))
        self.assertEqual(8 * 5 * 0.75, self.hp.getPrice([0, 1, 2, 3, 4]))

    def testSeveralDiscounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), self.hp.getPrice([0, 0, 1]))
        self.assertEqual(2 * (8 * 2 * 0.95), self.hp.getPrice([0, 0, 1, 1]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), self.hp.getPrice([0, 0, 1, 2, 2, 3]))
        self.assertEqual(8 + (8 * 5 * 0.75), self.hp.getPrice([0, 1, 1, 2, 3, 4]))

    def testEdgeCases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), self.hp.getPrice([0, 0, 1, 1, 2, 2, 3, 4]))
        self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
                     self.hp.getPrice([0, 0, 0, 0, 0,
                            1, 1, 1, 1, 1,
                            2, 2, 2, 2,
                            3, 3, 3, 3, 3,
                            4, 4, 4, 4]))
