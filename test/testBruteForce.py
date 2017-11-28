#  TestBruteForce.py
#
#  Unit tests for BruteForce.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys, os.path, unittest, io
from os.path import expanduser
home = expanduser("~/") # Saves the user's home directory
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import BruteForce


class BruteForceTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.home = expanduser("~") # Saves the user's home directory

        if (os.path.exists("output.json")):
            os.remove("output.json")

        self.expectedList = [{u'basic.matchall': {u'text': u'10/8/2017,1234,Tim', 
        u'subs': [{u'basic.datetime_patterns': {u'text': u'10/8/2017', 
        u'subs': [{u'datetime.simple_slash_date': {u'text': u'10/8/2017', u'pos': 1}}], 
        u'pos': 1}}, {u'basic.punctuation': {u'text': u',', u'pos': 10}}, 
        {u'common.number': {u'text': u'1234', u'subs': [{u'common.int': {u'text': u'1234', u'pos': 11}}], u'pos': 11}}, 
        {u'basic.punctuation': {u'text': u',', u'pos': 15}}, {u'common.word': {u'text': u'Tim', u'pos': 16}}], u'pos': 1}}, 
        {u'basic.matchall': {u'text': u'10/8/2017,1234,Tim', u'subs': [{u'basic.datetime_patterns': {u'text': u'10/8/2017', 
        u'subs': [{u'datetime.simple_slash_date': {u'text': u'10/8/2017', u'pos': 1}}], u'pos': 1}}, 
        {u'basic.punctuation': {u'text': u',', u'pos': 10}}, 
        {u'common.number': {u'text': u'1234', u'subs': [{u'common.int': {u'text': u'1234', u'pos': 11}}], u'pos': 11}},
        {u'basic.punctuation': {u'text': u',', u'pos': 15}}, {u'common.word': {u'text': u'Tim', u'pos': 16}}], u'pos': 1}}]

        self.json_file_path = home + "/Desktop/2017/CSC492/2017FallTeam11/output.json"
        
        self.bruteforce = BruteForce("test/SimpleData.csv")
        self.bruteforce.runBrute()
        

    def testFileExists(self):
        """Tests that the file exist"""
        assert self.bruteforce.filename == "test/SimpleData.csv"

    def testRunBrute(self):
        """Tests the runBrute function. Most of this function calls functions from rosie.py which isn't our code."""
        assert self.bruteforce.ROSIE_HOME == self.home + "/Desktop/rosie-pattern-language"
        assert self.bruteforce.config == """{"expression": "basic.matchall"}"""

        # Can't explicitly test these because they are different every time they are generated
        assert self.bruteforce.Rosie is not None
        assert self.bruteforce.engine is not None
        assert self.bruteforce.r is not None
        assert self.bruteforce.tbl is not None
        assert self.bruteforce.of is not None

    def testPrintMatchResults(self):
        """Test the print_match_results function."""
        self.bruteforce.print_match_results(self.bruteforce.r, self.bruteforce.of)
        assert self.bruteforce.list == self.expectedList
        print self.json_file_path
        assert os.path.exists(self.json_file_path)
        assert os.path.isfile(self.json_file_path)




if __name__ == "__main__":
    unittest.main() # run all tests
