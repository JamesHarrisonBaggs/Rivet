'''
PatternExtraction.py

PatternExtraction.py extracts the most deeply nested data type for each token of 
data in the input JSON file. The most deeply nested data type is the type that provides
the most specific information (e.g. IP_address is more specific than Word). The input
JSON file must have been created by Rosie (or Rivet using Rosie) for proper formatting.
The system combines token datatypes into line datatypes (patterns), which it recognizes 
on future lines and keeps track of how many times a line pattern has occured. The most
frequent line patterns are stored earlier in the Patterns tree, and are output to the console
first.

Authors: James Baggs, Xiaoyu Chen, Yuxu Yang

(Program outputs RPL files to /result/ directory and assumes datafiles are in /resource/)

Output:     Outputs a .txt file to the /result/ directory in the project. The output
            is named result.txt and contains a list of line patterns that are not 
            yet processed into .rpl format (FinalRecognition.py does this)

'''

import os, json, sys
import rosie
from Patterns import Patterns
from platform import node


class PatternExtraction:
    def __init__(self, filename, data):
        """Save the file name given from command-line."""
        self.filename = os.path.abspath(__file__+ "/../../") + "/result/" + filename
        self.root = Patterns("Root")
        self.current = self.root
        self.patternResult = list()
        self.numLines = 0
        self.resultfile = os.path.abspath(__file__+ "/../../") + "/result/" + "result.txt"
        self.data = data

    def runExtraction(self):
        """Runs the program."""
        ## Load the Json file and parse each object that is in the Json array.
        # with open(self.filename) as file:  ## Data file need to analyze
        print "Loading JSON data..."
        # data = json.load(file)
        self.numLines = len(self.data)
        print("\rPattern Extraction: Started")
        for i in range(len(self.data)):
            self.parseLine(self.data[i])
            ## After one line is finished, reset the cursor to root.
            self.current = self.root
            ## Progress bar
            percentage = round(float(i + 1) / (len(self.data)) * 100,1)
            print '\r[{0}] {1}%'.format('#'*(int(percentage)/2), percentage),
        print("")
        print("Pattern Extraction: Complete")
        print("")

        self.formPatFromTree(list(), self.root)
        self.printResult()


    def printResult(self):
        """Print the all patterns in the result list

           This function first sort patterns according to the times
           each number appears in the data file. The pattern appears 
           the most will be in the first index of the list. After the
           sorting of the list print all patterns name to the console
        """
        self.patternResult.sort(key=lambda x: x[len(x) - 1].count)
        f = open(self.resultfile, 'w')

        for i in reversed(self.patternResult):
            list = i
            for j in range(len(list)):
                 f.write(list[j].name+" ")
            # f.write(str(list[len(list) - 1].count))
            percentage = round(i[len(i) - 1].count / (float)(self.numLines) * 100, 2)
            f.write("$" + " ")
            f.write("," + str(percentage) + "\n" )
        f.close()

    def formPatFromTree(self, patterns, node):
        """Form patterns from trees

           A recursive function that form patterns from the tree
           and store each patterns into a final list.

           Args:
               patterns: a list of nodes, this list represents a single pattern
               node: current node the function is working on

        """
        ## Remove the Root name from the list since it's not a actual pattern name
        if (node.name != "Root"):
            patterns.append(node)
        ## When current node has no more children which means this is
        ## the end of  pattern, other wise keep going.
        if (len(node.next) == 0):
            self.patternResult.append(patterns)
            
        else:
            count = 0
            for i in range(len(node.next)):
                count += node.next[i].count
                newList = list(patterns)
                self.formPatFromTree(newList, node.next[i])

            if (node.count - count != 0 and len(patterns) != 0):
                node.count = node.count - count
                self.patternResult.append(patterns)

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
            if (nextIndex >= 0):
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