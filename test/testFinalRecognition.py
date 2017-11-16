#  TestFinalRecognition.py
#
#  Unit tests for FinalRecognition.py
#
#  Authors: Yuxu Yang, Xiaoyu Chen, James Baggs
import sys, os.path, unittest, os, json, sys
from os.path import expanduser
home = expanduser("~") # Saves the user's home directory
sys.path.append(home + '/Desktop/2017/CSC492/2017FallTeam11/src') # Makes the src folder accessible for testing
from FinalRecognition import FinalRecognition
import mock
from PatternExtraction import PatternExtraction
from BruteForce import BruteForce
from mock import MagicMock
from mock import Mock


class FinalRecognitionTestCase(unittest.TestCase):
    global m
    def setUp(self):
        self.bruteforce = BruteForce("test/testDataStructure.csv")
        self.bruteforce.runBrute()

        self.patExtract = PatternExtraction("output.json")
        self.patExtract.runExtraction()

        if(os.path.exists("result.rpl")):
            os.remove('result.rpl')
        self.finalRecog = FinalRecognition("test/testDataStructure.csv")

    # there are three user input, '1 2' means user choose number 1 and number 2 for build customized rpl file,
    # result.rpl is the name, result is the pattern name
    m = Mock()
    m.side_effect = ['1 2', 'result.rpl', 'result']
    def testRun(self):
        with mock.patch('__builtin__.raw_input', m):
            self.finalRecog.run()
        # Can't explicitly test these because they are different every time they are generated
            assert self.finalRecog.filename is not None
            ## Json objects for all line.
            assert self.finalRecog.list is not None
            assert self.finalRecog.patternList is not None
            assert os.path.exists("result.rpl")
            assert os.path.isfile("result.rpl")


    # test the finalRecognition program RunNoUI method, which input a prunePctentage, and output the match rate based on it.
    # the example below gives 100 percentage of match rate from the example test file.
    k = Mock()
    k.side_effect = ['1 2', 'result.rpl', 'result']
    def testNoUI(self):
        self.assertEqual(self.finalRecog.runNoUI(1), 100)
        assert os.path.exists("auto.rpl")
        assert os.path.isfile("auto.rpl")

    def tearDown(self):
        os.remove("output.json")
        os.remove("result.txt")
        if (os.path.exists("result.rpl")):
            os.remove('result.rpl')
        if (os.path.exists("auto.rpl")):
            os.remove('auto.rpl')


if __name__ == "__main__":
    unittest.main()