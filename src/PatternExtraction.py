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

############
#GLOBAL VARS
root = Patterns("Root") ## Root node of the tree structure.
current = root ## A node cursor represents current node is on.
############

class PatternExtraction:
    
    def __init__(self, filename):
        """Save the file name given from command-line."""
        self.filename = filename
    
    def runExtraction(self):
        """Runs the program."""
        ## Load the Json file and parse each object that is in the Json array.
        with open(self.filename) as file: ## Data file need to analyze 
            data = json.load(file)
            for i in range(len(data)):
                print data[i]
                self.parseLine(data[i])
                ## After one line is finished, reset the cursor to root.
                current = root

        ## Function call that print the tree
        self.printPatter(root)

    def parseLine(self, jsonData):
        """Extract pattern names and put them in a tree
            
            A recursive function that get a single Json object, extract the 
            deepest sub pattern key convert it to a string of pattern name. 
            Using the pattern name to construct a node object for each pattern 
            name, then add each object into the tree.
       
            Args:
                jsonData: a single json object(structure)
        """
        
        global current #Use the global variable current
        global root #Use the global variable root
        if 'subs' not in jsonData.values()[0]:
            # Convert json key object to a string
            strKey = json.dumps(jsonData.keys())
            result = strKey.split('\"')[1].strip()
            # Construct a new node object with pattern name.
            node = Patterns(result)
            nextIndex = current.isInList(node)
            # Check if this pattern is already exist in the tree,
            # if already exit get the index of this node then 
            # move current curse to the next node.
            if(nextIndex >= 0):
                current = current.next[nextIndex]
                current.count += 1
            else:
            ## If pattern does not exist in current node's children
            # list
                nextIndex = current.addNode(node)
                current = current.next[nextIndex]
                current.count += 1
        else: 
            ## Go deeper into the json structure if
            ## current pattern is not the deepest.
            data = jsonData.values()[0]['subs']
            for i in range(len(data)):
                sub = data[i]
                self.parseLine(sub)

    def printPatter(self, rootNode):
        """ Print each level of the tree
    
            This function is only print each level of the tree.
            Each level of the tree will print as a single line
            in the terminal
        
            Args:
                rootNode: root node of the tree structure 
        """
        ## Current level of the tree
        currlvl = list()
        ## Add the root node the current level list.
        currlvl.append(rootNode)
        ## Next level of the tree.
        nextlvl = list()
        ## Add all children of current node to next level list
        while currlvl:
            for i in range(len(currlvl)):
                for j in range(len(currlvl[i].next)):
                    nextlvl.append(currlvl[i].next[j])
            ## Print current level pattern names, and numbers of
            ## time they have appear in this level
            for i in range(len(currlvl)):
                print currlvl[i].name, currlvl[i].count, 
            print ""
            ## Move the current level cursor to next level.
            currlvl = nextlvl
            nextlvl = []

if __name__ == "__main__":
    extract = PatternExtraction(sys.argv[1])
    extract.runExtraction()