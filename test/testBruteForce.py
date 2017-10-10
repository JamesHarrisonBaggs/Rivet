#  TestBruteForce.py
#
#  Unit tests for BruteForce.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys
from os.path import expanduser
home = expanduser("~/Desktop/2017/CSC492") # Saves the user's home directory
sys.path.append(home + '/2017FallTeam11/src') # Makes the src folder accessible for testing
import unittest
from BruteForce import BruteForce

class RosieHomeTestCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        self.bruteforce = BruteForce()


if __name__ == "__main__":
    bruteTest = BruteForce("SimpleData.csv")
    unittest.main() # run all tests