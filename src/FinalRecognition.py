#  BruteForce.py
#
#  A program that uses Rosie's "match all" functionality
#  to match parsed data against Rosie's library of patterns.
#
#  Code copied and modified from rtest.py.
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import os, json, sys
import rosie


class BruteForce:
    def __init__(self, filename):
        """Initialize the variables."""
        self.filename = filename
        self.ROSIE_HOME = None
        self.Rosie = None
        self.engine = None
        self.config = None
        self.r = None
        self.tbl = None
        self.of = None
        ## Json objects for all line.
        self.list = []
        self.PatternList = []

    def runPattern(self, matchfile):
        """Runs the program."""
        self.ROSIE_HOME = os.getenv("ROSIE_HOME")
        if not self.ROSIE_HOME:
            print "Environment variable ROSIE_HOME not set.  (Must be set to the root of the rosie directory.)"
            sys.exit(-1)

        self.Rosie = rosie.initialize(self.ROSIE_HOME, self.ROSIE_HOME + "/ffi/librosie/librosie.so")
        # print "Rosie library successfully loaded"

        self.engine = self.Rosie.engine()
        # print "Obtained a rosie matching engine:", self.engine, "with id", self.engine.id

        self.config = json.dumps({'encode': 'json'})
        self.r = self.engine.configure(self.config)
        # if not self.r: print "Engine reconfigured to look for digits\n"
        # else: print "Error reconfiguring engine!", r

        self.r = self.engine.inspect()
        # print self.r

        self.tbl = json.loads(self.r[0])
        # print "Return from inspect_engine is:", str(self.tbl)

        self.r = self.engine.load_manifest("$sys/MANIFEST")
        # for s in self.r: print s

        ## list of current pattern match result
        currentPatList = list()
        ##Use the basic.matchall to parse all data
        self.config = json.dumps({'expression': matchfile})
        self.r = self.engine.configure(self.config)
        number = 0
        with open(self.filename) as file:  ## Data file need to analyize
            ## This is the output json file that contains all pattern that matched
            for line in file:
                # print(line[-4:])
                self.r = self.engine.match(line, None)
                self.print_match_results(self.r, currentPatList)
                number += 1  ## This is just keep tracking lines numbers
            self.list.append(currentPatList)
            self.PatternList.append(matchfile)

    def print_match_results(self, r, currentList):
        match = json.loads(r[0]) if r else False
        currentList.append(match)
        leftover = json.loads(r[1])
        # currentList.append(leftover)

    def checkResult(self):
        ##reading the file from result.txt to
        resultfile = "result.txt"
        with open(resultfile) as f:
            content = f.read().splitlines()
            for i in content:
                self.runPattern(i)

    def reportNumber(self):
        """Report how many data each pattern has matched in percentage

           This function returns strings to report how many data each pattern
           is able to match in both number count and the ratio

        """
        for i in range(len(self.list)):
            count = 0
            for j in self.list[i]:
                if (j != False):
                    count += 1
            percentage = round(float(count) / len(self.list[i]) * 100, 2)
            strReport = str(i) + " has " + str(count) + " matched " + str(percentage) + "% of total data"
            print strReport

    def CustomizedPatternCreation(self):
        print "What are the patterns you want to choose "
        sequence = raw_input("<pattern number> <pattern number> \n example: 1 2 \n").split()
        filename = raw_input("Give the name to your customized rpl file \n example: result.rpl \n")
        patternName = raw_input("Give the name to your customized patternName \n example: customer \n")
        choosen = []
        for i in sequence:
            choosen.append(int(i))
        with open(filename, "w") as cof:
            cof.write(patternName+ " = ")
            s = ' / '
            sqe = []
            for i in range(len(choosen)):
                sqe.append("(" + str(self.PatternList[choosen[i]]) + ")")
            s = s.join(sqe)
            cof.write(s)


if __name__ == "__main__":
    brute = BruteForce(sys.argv[1])
    brute.checkResult()
    with open("resultFinal.json", "w") as of:
        json.dump(brute.list, of, indent=2)
    brute.reportNumber()
    brute.CustomizedPatternCreation()