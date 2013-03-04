import os
import unittest

from measures.rankedlist import *

class RankedListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = ['a','b','c','d','e']
        self.list2 = ['b','a','c','d','e']
        self.list3 = ['a','b','c','e','d']
    
    def test_ao(self):
        score1 = AverageOverlap.score(self.list1, self.list2)
        self.assertEqual(score1, 0.8)
        score2 = AverageOverlap.score(self.list1, self.list3)
        self.assertEqual(score2, 0.95)
        
        