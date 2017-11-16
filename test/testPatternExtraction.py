#  TestPatternExtraction.py
#
#  Unit tests for PatternExtraction.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys,os
from os.path import expanduser

home = expanduser("~")  # Saves the user's home directory
sys.path.append(home + '/Desktop/2017/CSC492/2017FallTeam11/src')  # Makes the src folder accessible for testing
import unittest
from PatternExtraction import PatternExtraction
from BruteForce import BruteForce


class PatternsTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        if os.path.isfile("./result.txt"):
            os.remove("result.txt")
        # This must run first to create the output.json file
        self.bruteforce = BruteForce("test/testDataStructure.csv")
        self.bruteforce.runBrute()


        self.patExtract = PatternExtraction("output.json")
        self.patExtract.runExtraction()

    def testFileExists(self):
        """Tests that the file exist"""
        assert self.patExtract.filename == "output.json"

    def testRunExtraction(self):
        """Tests the runExtraction function"""
        assert os.path.exists("result.txt")
        assert os.path.isfile("result.txt")



if __name__ == "__main__":
    unittest.main()  # run all tests