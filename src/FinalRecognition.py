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



class FinalRecognition:

    class PatternReport:
        '''A inner class help store pattern and its match percentage

           Encapsulating pattern and its match result into a object

           Args:
                pattern the actual pattern
                percentage number of percentage this pattern matched in sample data
        '''
        def __init__(self, pattern, percentage):
            self.pattern = pattern
            self.percentage = percentage

    def __init__(self, filename):
        """Initialize the variables."""
        self.filename = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/resource/" + filename
        self.ROSIE_HOME = None
        self.Rosie = None
        self.engine = None
        self.config = None
        self.r = None
        self.tbl = None
        self.RPLFileName = None
        self.PatternName = None
        self.Sequence = None
        ## Json objects for all line.
        self.list = []
        self.patternList = []
        self.resultfile = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/result/"+ "result.txt"

    def checkResult(self):
        ##reading the file from result.txt to
        with open(self.resultfile) as f:
            content = f.read().splitlines()
            for i in content:
                ## Split the string to get the pattern and match percentage
                tempPat = i.split(",")
                ## Encapsulating information into a object
                patRept = self.PatternReport(tempPat[0], float(tempPat[1]))
                self.patternList.append(patRept)
                # self.runPattern(i)

    def reportNumber(self):
        """Report how many data each pattern has matched in percentage

           This function returns strings to report how many data each pattern
           is able to match in both number count and the ratio

        """
        print("Pattern matching report:")
        for i in range(len(self.patternList)):
            pat = self.patternList[i]
            print("Pattern "+ str(i) + " matched " + str(pat.percentage) + "% of sample file")
        print("")

    def CustomizedPatternCreation(self):
        error = True
        while(error != False):
            self.Sequence = raw_input("What are the patterns you want to choose \n<pattern number> <pattern number> \n example: 1 2 \n")
            # print self.Sequence
            self.Sequence = self.Sequence.split()
            choosen = []
            try:
                for i in self.Sequence:
                    i = int(i)
                    if(i <= len(self.patternList) - 1 and i >= 0):
                        choosen.append(i)
                        error = False
                    else:
                        error = True
                if(error):
                    raise Exception("Invalid index.")
            except ValueError:
                print("Please input Integer value.")
            except Exception as err:
                print (err.args)
        self.RPLFileName = raw_input("Give the name to your customized rpl file \n example: result.rpl \n")
        self.RPLFileName = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/result/" + self.RPLFileName
        # print self.RPLFileName
        self.PatternName = raw_input("Give the name to your customized patternName \n example: customer \n")
        # print self.PatternName
        with open(self.RPLFileName, "w") as cof:
            cof.write(self.PatternName+ " = ")
            s = ' / '
            sqe = []
            for i in range(len(choosen)):
                sqe.append("(" + str(self.patternList[choosen[i]].pattern) + ")")
            s = s.join(sqe)
            cof.write(s)

    def run(self):
        self.checkResult()
        # with open("resultFinal.json", "w") as of:
        #     json.dump(self.list, of, indent=2)
        self.reportNumber()
        self.CustomizedPatternCreation()

    #Automatically generates RPL given a prune Percentage.
    #Returns match percentage
    def runNoUI(self, prunePct):
        self.checkResult()
        self.reportNumber()
        self.RPLFileName = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/result/" + "auto.rpl"
        self.PatternName = "auto"
        totalPct = 0.0
        with open(self.RPLFileName, "w") as cof:
            cof.write(self.PatternName+ " = ")
            s = ' / '
            sqe = []
            for x in range(len(self.patternList)):
                percentage = self.patternList[x].percentage
                if (int(prunePct) < int(percentage)):
                    totalPct += percentage
                    sqe.append("(" + str(self.patternList[x].pattern) + ")")
            s = s.join(sqe)
            cof.write(s)
        return totalPct

if __name__ == "__main__":
    final = FinalRecognition(sys.argv[1])
    final.run()