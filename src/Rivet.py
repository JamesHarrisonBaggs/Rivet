'''
Rivet.py

Rivet.py is the Rosie Pattern Language (RPL) file-pattern generation system. It
analyzes a semistructured data file in a format such as CSV, HTML, or TXT and
produces a .rpl file which can be used with Rosie (or FinalDataPattern.py) to
extract data from the original input file much faster than would be capable by
Rosie's default Brute Force extraction. It has two main operating modes: Automatic
and User Interface. If a pattern prune percentage is specified, the system will 
Automatically extract data into its patterns, otherwise a User Interface will
be displayed to allow users to select which patterns they would like save in .rpl

Authors: James Baggs, Xiaoyu Chen, Yuxu Yang

(Program outputs RPL files to /result/ directory and assumes datafiles are in /resource/)
Usage:      >python Rivet.py <options> <datafile>
Examples:   >python Rivet.py NewDataSet.csv
                Uses 100% of datafile, User Interface On
            >python Rivet.py -s 10 NewDataSet.csv
                Samples 10% of datafile, User Interface On
            >python Rivet.py -s 10 -p 1 NewDataSet.csv
                Samples 10% of data, automatically prunes patterns that mach less
                than 1% of data. Saves resulting pattern "auto" to /result/auto.rpl
Output:     Outputs a .rpl file to the /result/ directory in the project. The output
            is named auto.rpl when a prune percentage is specified, and is manually
            named by the user in UI mode.

'''
import getopt
import sys
import os
from sample import sample
from BruteForce import BruteForce
from PatternExtraction import PatternExtraction
from FinalRecognition import FinalRecognition

class Rivet:
    def __init__(self, prunePct, sampleSize, inputFile):
        """Initialize the variables."""
        self.prunePct = prunePct
        self.sampleSize = sampleSize
        self.inputFile = inputFile

        sampler = sample(self.sampleSize, self.inputFile)
        sampler.sampling()

        dataParser = BruteForce(os.path.basename(os.path.normpath(sampler.outputfile)))
        data = dataParser.runBrute()

        extractor = PatternExtraction(os.path.basename(os.path.normpath(dataParser.outputfile)), data)
        extractor.runExtraction()

    def runUIGenerator(self):
                ## Modu

        rplGenerator = FinalRecognition(self.inputFile)
        rplGenerator.run()

    def runGenerator(self):
        rplGenerator = FinalRecognition(self.inputFile)
        return rplGenerator.runNoUI(self.prunePct)


    def getRuntime(self):
        print "hi"
        

    def getMatchPct(self):
        ##
        return self.runGenerator()

if __name__ == "__main__":
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 's:p:', ['sampleSize=', 'prunePct='])
    except getopt.GetoptError as err:
        print err
        sys.exit(0)

    size = 100
    prunePct = -1
    for opt, arg in options:
        if opt in ('--sampleSize', '-s'):
            size = arg
        if opt in ('--prunePct', '-p'):
            prunePct = arg
    numArgs = len(remainder)
    inputFile = ''
    # No input file
    if numArgs == 0:
        print("No input file specified")
        exit(0)
    elif (numArgs == 1):
        if remainder[0].upper() == "HELP":
            print("Help Page")
        else:
            inputFile = remainder[0] 
    Rivet = Rivet(prunePct, size, inputFile)
    if(prunePct < 0):
        Rivet.runUIGenerator()
    else:
        print "match pct: " + str(Rivet.getMatchPct())