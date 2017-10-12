"""
    A program reads Json file that is output from rosie,
    it extracts the deepest pattern from the Json strucutre
    then create node objects for each pattern and put them into
    a tree data structure.

"""

import os, json, sys
import rosie
from Patterns import Patterns
from platform import node

class PatternExtraction:
    
    def __init__(self, filename):
        """Save the file name given from command-line."""
        self.filename = filename
        self.root = Patterns("Root")
        self.current = self.root
    
    def runExtraction(self):
        """Runs the program."""
        ## Load the Json file and parse each object that is in the Json array.
        with open(self.filename) as file: ## Data file need to analyze 
            data = json.load(file)
            for i in range(len(data)):
                self.parseLine(data[i])
                ## After one line is finished, reset the cursor to root.
                self.current = self.root

        ## Function call that print the tree
#         self.printPatter(self.root)
        self.printTree("", self.root)

    def printTree(self, patterns, node):
        patterns = patterns + node.name + " "
        if(len(node.next) == 0):
            print patterns
            print
        else:
            count = 0
            for i  in range(len(node.next)):
                count += node.next[i].count
                self.printTree(patterns, node.next[i])
            
            if(node.count - count !=0):
                print patterns
        
    
    def parseLine(self, jsonData):
        """Extract pattern names and put them in a tree
            
            A recursive function that get a single Json object, extract the 
            deepest sub pattern key convert it to a string of pattern name. 
            Using the pattern name to construct a node object for each pattern 
            name, then add each object into the tree.
       
            Args:
                jsonData: a single json object(structure)
        """
        
#         global current #Use the global variable current
#         global root #Use the global variable root
        if 'subs' not in jsonData.values()[0]:
            # Convert json key object to a string
            strKey = json.dumps(jsonData.keys())
            result = strKey.split('\"')[1].strip()
            # Construct a new node object with pattern name.
            node = Patterns(result)
            nextIndex = self.current.isInList(node)
            # Check if this pattern is already exist in the tree,
            # if already exit get the index of this node then 
            # move current curse to the next node.
            if(nextIndex >= 0):
                self.current = self.current.next[nextIndex]
                self.current.count += 1
            else:
            ## If pattern does not exist in current node's children
            # list
                nextIndex = self.current.addNode(node)
                self.current = self.current.next[nextIndex]
                self.current.count += 1
        else: 
            ## Go deeper into the json structure if
            ## current pattern is not the deepest.
            data = jsonData.values()[0]['subs']
            for i in range(len(data)):
                sub = data[i]
                self.parseLine(sub)


if __name__ == "__main__":
    extract = PatternExtraction(sys.argv[1])
    extract.runExtraction()