'''
FinalRecognition.py

FinalRecognition.py is the final step in the Rivet system which uses the
extracted patterns from PatternExtraction.py to generate the final RPL file.
run() and runNoUI() are called depending on whether or not a prune percentage
was specified in Rivet, where run() allows the user to specify patterns and
name the RPL file through the command line user interface.

Authors: James Baggs, Xiaoyu Chen, Yuxu Yang

Output:     Outputs a .rpl file to the /result/ directory in the project. The output
            is named auto.rpl when a prune percentage is specified, and is manually
            named by the user in UI mode.

'''

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
        self.filename = os.path.abspath(os.path.abspath(__file__+ "/../../")) + "/resource/" + filename
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
        self.resultfile = os.path.abspath(os.path.abspath(__file__+ "/../../")) + "/result/result.txt"

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
        self.RPLFileName = os.path.abspath(os.path.abspath(__file__+ "/../../")) + "/result/" + self.RPLFileName
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
        self.RPLFileName = os.path.abspath(os.path.abspath(__file__+ "/../../")) + "/result/" + "auto.rpl"
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