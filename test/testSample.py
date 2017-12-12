from unittest import TestCase


import sys, os.path, unittest, io, os

from src import sample

class SampleTestCase(unittest.TestCase):

    def setUp(self):
        self.sampler = sample(10,"NewDataSet.csv")

    def test_sampling(self):
        assert self.sampler.inputfile == os.path.abspath(__file__ + "/../../") + "/resource/NewDataSet.csv"
        assert self.sampler.outputfile == os.path.abspath(__file__ + "/../../") + "/resource/sample_NewDataSet.csv"
        assert self.sampler.samplePercentage == 10
        self.sampler.sampling()
        num_lines = sum(1 for line in open(os.path.abspath(__file__ + "/../../") + "/resource/NewDataSet.csv"))
        target_lines = sum(1 for line in open(os.path.abspath(__file__ + "/../../") + "/resource/sample_NewDataSet.csv"))
        assert target_lines == int(num_lines * (self.sampler.samplePercentage/100.0))

