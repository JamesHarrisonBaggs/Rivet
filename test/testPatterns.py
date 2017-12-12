#  TestPatterns.py
#
#  Unit tests for Patterns.py
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import sys
from os.path import expanduser

import unittest
from src import Patterns

class PatternsTestCase(unittest.TestCase):
    
    def setUp(self):
        """Call before every test case."""
         # Create the root node of the tree
        root = Patterns("Root")
        

    def testAddNodesToRoot(self):
        """Test for adding two nodes to the root node."""
        root = Patterns("Root")
        firstNode = Patterns("1") # First node to be added
        firstNode.count += 1
        if root.isInList(firstNode) == -1:
            root.addNode(firstNode)
        assert root.isInList(firstNode) != -1 # Assert that it exists in the list

        secondNode = Patterns("2") # Second node to be added
        secondNode.count += 1
        if root.isInList(secondNode) == -1:
            root.addNode(secondNode)
        assert root.isInList(secondNode) != -1 # Assert that it exists in the list

        # Make sure that the root node exists
        assert  root.name == "Root"
        assert  root.count == 0
        assert len(root.next) == 2

        # Make sure that the first child node exists
        assert  firstNode.name == "1"
        assert  firstNode.count == 1
        assert len( firstNode.next) == 0

        # Make sure that the second child node exists
        assert  secondNode.name == "2"
        assert  secondNode.count == 1
        assert len( secondNode.next) == 0
      
    
    def testAddNodesToChildren(self):
        """Test for adding a node to an existing child node."""
        root = Patterns("Root")
        firstNode = Patterns("1") # First node to be added
        firstNode.count += 1
        if root.isInList(firstNode):
            root.addNode(firstNode)
        assert root.isInList( firstNode) != -1 # Assert that it exists in the list

        secondNode = Patterns("2") # Second node to be added
        secondNode.count += 1
        if firstNode.isInList(secondNode) == -1:
            firstNode.addNode(secondNode)
        assert firstNode.isInList(secondNode) != -1 # Assert that it exists in the list

        # Make sure that the root node exists
        assert root.name == "Root"
        assert root.count == 0
        assert len(root.next) == 1
        assert root.next[0].name == "1"
        
        # Make sure that the first child node exists
        assert firstNode.name == "1"
        assert firstNode.count == 1
        assert len(firstNode.next) == 1
        assert firstNode.next[0].name == "2"

        # Make sure that the second child node exists
        assert secondNode.name == "2"
        assert secondNode.count == 1
        assert len(secondNode.next) == 0

if __name__ == "__main__":
    unittest.main() # run all tests