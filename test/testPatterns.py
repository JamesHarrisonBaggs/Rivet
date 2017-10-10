#  TestPatterns.py
#
#  Unit tests for Patterns.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys
from os.path import expanduser
home = expanduser("~/Desktop/2017/CSC492") # Saves the user's home directory
sys.path.append(home + '/2017FallTeam11/src') # Makes the src folder accessible for testing
import unittest
from Patterns import Patterns

class PatternsTestCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        self.root = Patterns("Root") # Create the root node of the tree

    def testAddNodesToRoot(self):
        """Test for adding two nodes to the root node."""

        self.firstNode = Patterns("1") # First node to be added
        self.firstNode.count += 1
        if self.root.isInList(self.firstNode):
            self.root.addNode(self.firstNode)
        assert self.root.isInList(self.firstNode) != -1 # Assert that it exists in the list

        self.secondNode = Patterns("2") # Second node to be added
        self.secondNode.count += 1
        if self.root.isInList(self.secondNode) == -1:
            self.root.addNode(self.secondNode)
        assert self.root.isInList(self.secondNode) != -1 # Assert that it exists in the list

        # Make sure that the root node exists
        assert self.root.name == "Root"
        assert self.root.count == 0
        assert len(self.root.next) == 2
        
        # Make sure that the first child node exists
        assert self.firstNode.name == "1"
        assert self.firstNode.count == 1
        assert len(self.firstNode.next) == 0

        # Make sure that the second child node exists
        assert self.secondNode.name == "2"
        assert self.secondNode.count == 1
        assert len(self.secondNode.next) == 0
        
    def testAddNodesToChildren(self):
        """Test for adding a node to an existing child node."""
        
        self.firstNode = Patterns("1") # First node to be added
        self.firstNode.count += 1
        if self.root.isInList(self.firstNode):
            self.root.addNode(self.firstNode)
        assert self.root.isInList(self.firstNode) != -1 # Assert that it exists in the list

        self.secondNode = Patterns("2") # Second node to be added
        self.secondNode.count += 1
        if self.firstNode.isInList(self.secondNode) == -1:
            self.firstNode.addNode(self.secondNode)
        assert self.firstNode.isInList(self.secondNode) != -1 # Assert that it exists in the list

        # Make sure that the root node exists
        assert self.root.name == "Root"
        assert self.root.count == 0
        assert len(self.root.next) == 1
        assert self.root.next[0].name == "1"
        
        # Make sure that the first child node exists
        assert self.firstNode.name == "1"
        assert self.firstNode.count == 1
        assert len(self.firstNode.next) == 1
        assert self.firstNode.next[0].name == "2"

        # Make sure that the second child node exists
        assert self.secondNode.name == "2"
        assert self.secondNode.count == 1
        assert len(self.secondNode.next) == 0

if __name__ == "__main__":
    unittest.main() # run all tests