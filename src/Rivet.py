import getopt
import sys
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

        dataParser = BruteForce(sampler.outputfile)
        dataParser.runBrute()

        extractor = PatternExtraction(dataParser.outputfile)
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