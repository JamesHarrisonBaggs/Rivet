#  TestPatternExtraction.py
#
#  Unit tests for PatternExtraction.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys
from os.path import expanduser
home = expanduser("~") # Saves the user's home directory
sys.path.append(home + '/2017FallTeam11/src') # Makes the src folder accessible for testing
import unittest
from PatternExtraction import PatternExtraction 
from BruteForce import BruteForce

class PatternsTestCase(unittest.TestCase):
    
    def setUp(self):
        """Call before every test case."""

        # This must run first to create the output.json file
        self.bruteforce = BruteForce("SimpleData.csv")
        self.bruteforce.runBrute()

        self.patExtract = PatternExtraction("output.json")

    def testFileExists(self):
        """Tests that the file exist"""
        assert self.patExtract.filename == "output.json"

if __name__ == "__main__":
    unittest.main() # run all tests