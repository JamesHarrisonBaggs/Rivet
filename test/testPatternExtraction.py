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
import PatternExtraction

class PatternsTestCase(unittest.TestCase):
    
    def setUp(self):
        """Call before every test case."""
        self.patExtract = PatternExtraction("SimpleData.csv")
        

    


if __name__ == "__main__":
    unittest.main() # run all tests