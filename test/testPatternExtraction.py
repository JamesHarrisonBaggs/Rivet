#  TestPatternExtraction.py
#
#  Unit tests for PatternExtraction.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys,os,unittest
from os.path import expanduser


sys.path.insert(0, os.path.abspath(__file__+"/.."))
from src import PatternExtraction
from src import BruteForce


class PatternsTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        if os.path.isfile("./result.txt"):
            os.remove("result.txt")
        # This must run first to create the output.json file
        self.bruteforce = BruteForce("testDataStructure.csv")
        data = self.bruteforce.runBrute()


        self.patExtract = PatternExtraction("output.json", data)
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