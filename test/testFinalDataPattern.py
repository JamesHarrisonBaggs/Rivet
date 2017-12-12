import sys, os.path, unittest, io, os

from src import FinalDataPattern
from src import Rivet
import mock, os
from mock import Mock

class FinalDataPatternTestCase(unittest.TestCase):
    ### creating customized rpl file.
    global customizedResultLocation
    customizedResultLocation = os.path.abspath(os.path.abspath(__file__ + "/../../")) + "/result/customizedResult.json"
    global m
    m = Mock()
    m.side_effect = ['1 2', 'self.rpl', 'self']
    def setUp(self):
        with mock.patch('__builtin__.raw_input', m):
            self.rivet = Rivet(1,10,"NewDataSet.csv")
            self.rivet.runUIGenerator()

    def test_Customized_RPL(self):
        self.finalData = FinalDataPattern("NewDataSet.csv", "self.rpl", "self")
        self.finalData.runCustomizedPattern()
        num_lines = sum(1 for line in open(os.path.abspath(__file__ + "/../../") + "/resource/NewDataSet.csv"))
        assert self.finalData.matchRate == int(num_lines * (47.06/100.0))
        assert os.path.exists(customizedResultLocation)
        assert os.path.isfile(customizedResultLocation)

    def tearDown(self):
        os.remove(os.path.abspath(__file__ + "/../../") + "/result/output.json")
        os.remove(os.path.abspath(__file__ + "/../../") + "/result/result.txt")
        os.remove(os.path.abspath(__file__ + "/../../") + "/result/self.rpl")
        if os.path.exists(customizedResultLocation):
            os.remove(customizedResultLocation)
