from unittest import TestCase


import sys, os.path, unittest, io, os

from src import Rivet
import mock
from mock import MagicMock
from mock import Mock

class RivetTestCase(unittest.TestCase):
    global autoPath
    autoPath = os.path.abspath(os.path.abspath(__file__ + "/../../")) + "/result/auto.rpl"
    global resultPath
    resultPath = os.path.abspath(os.path.abspath(__file__ + "/../../")) + "/result/result.rpl"

    def setUp(self):
        self.rivet = Rivet(1,10,"NewDataSet.csv")

    def test_file_location(self):
        assert self.rivet.inputFile == "NewDataSet.csv"
        assert self.rivet.prunePct == 1
        assert self.rivet.sampleSize == 10

    def test_rivet_with_pruneSize(self):
        self.rivet.runGenerator()
        assert self.rivet.getMatchPct() == 100.0
        assert os.path.exists(autoPath)
        assert os.path.isfile(autoPath)


    global m
    m = Mock()
    m.side_effect = ['1 2', 'result.rpl', 'result']
    def test_rivet_without_pruneSize(self):
        with mock.patch('__builtin__.raw_input', m):
            self.rivet.runUIGenerator()
            assert os.path.exists(resultPath)
            assert os.path.isfile(resultPath)

    def tearDown(self):
        os.remove(os.path.abspath(__file__+ "/../../")+"/result/output.json")
        os.remove(os.path.abspath(__file__+ "/../../")+"/result/result.txt")
        os.remove(os.path.abspath(__file__ + "/../../") + "/result/NewDataSet.csv_sample")

        if os.path.exists(autoPath):
            os.remove(autoPath)
        if os.path.exists(resultPath):
            os.remove(resultPath)


