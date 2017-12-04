#  TestFinalRecognition.py
#
#  Unit tests for FinalRecognition.py
#
#  Authors: Yuxu Yang, Xiaoyu Chen, James Baggs
import sys, os.path, unittest, os, json, sys
from os.path import expanduser
from src import FinalRecognition
import mock
from src import PatternExtraction
from src import BruteForce
from mock import MagicMock
from mock import Mock


class FinalRecognitionTestCase(unittest.TestCase):
    global m
    def setUp(self):
        self.bruteforce = BruteForce("testDataStructure.csv")
        print self.bruteforce.filename
        data = self.bruteforce.runBrute()

        self.patExtract = PatternExtraction("output.json",data)
        self.patExtract.runExtraction()

        resultPath = os.path.abspath(__file__+ "/../../")+"/result/result.rpl"

        if(os.path.exists(resultPath)):
            os.remove(resultPath)
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
            resultRPL = os.path.abspath(os.path.abspath(__file__ + "/../../")) + "/result/result.rpl"
            assert os.path.exists(resultRPL)
            assert os.path.isfile(resultRPL)


    # test the finalRecognition program RunNoUI method, which input a prunePctentage, and output the match rate based on it.
    # the example below gives 100 percentage of match rate from the example test file.
    k = Mock()
    k.side_effect = ['1 2', 'result.rpl', 'result']
    def testNoUI(self):
        self.assertEqual(self.finalRecog.runNoUI(1), 100)
        autoPath = os.path.abspath(os.path.abspath(__file__ + "/../../"))+"/result/auto.rpl"
        assert os.path.exists(autoPath)
        assert os.path.isfile(autoPath)

    def tearDown(self):
        os.remove(os.path.abspath(__file__+ "/../../")+"/result/output.json")
        os.remove(os.path.abspath(__file__+ "/../../")+"/result/result.txt")
        if (os.path.exists("result.rpl")):
            os.remove('result.rpl')
        if (os.path.exists("auto.rpl")):
            os.remove('auto.rpl')


if __name__ == "__main__":
    unittest.main()