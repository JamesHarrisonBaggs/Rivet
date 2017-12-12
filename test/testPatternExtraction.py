#  TestPatternExtraction.py
#
#  Unit tests for PatternExtraction.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys,os,unittest
from os.path import expanduser

from src import PatternExtraction
from src import BruteForce


class PatternsTestCase(unittest.TestCase):
    global resultLocation
    global jsonOutputLocation
    resultLocation = os.path.abspath(__file__ + "/../../") + "/result/result.txt"
    jsonOutputLocation = os.path.abspath(__file__ + "/../../") + "/result/output.json"

    def setUp(self):
        """Call before every test case."""

        if os.path.isfile(resultLocation):
            os.remove(resultLocation)
        # This must run first to create the output.json file
        self.bruteforce = BruteForce("testDataStructure.csv")
        data = self.bruteforce.runBrute()


        self.patExtract = PatternExtraction("output.json", data)
        self.patExtract.runExtraction()

    def testFileExists(self):
        """Tests that the file exist"""
        assert self.patExtract.filename == jsonOutputLocation

    def testRunExtraction(self):
        """Tests the runExtraction function"""
        assert os.path.exists(resultLocation)
        assert os.path.isfile(resultLocation)

    def tearDown(self):

        os.remove(jsonOutputLocation)
        os.remove(resultLocation)

        if (os.path.exists(os.path.abspath(__file__ + "/../../") + "/result/result.rpl")):
            os.remove(os.path.abspath(__file__ + "/../../") + "/result/result.rpl")
        if (os.path.exists(os.path.abspath(__file__ + "/../../") + "/result/auto.rpl")):
            os.remove(os.path.abspath(__file__ + "/../../") + "/result/auto.rpl")




if __name__ == "__main__":
    unittest.main()  # run all tests