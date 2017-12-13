import getopt
import sys
from os import listdir
from os.path import isfile, join
import os.path
from matplotlib import pyplot as plt

# sys.path.append('/home/james/2017FallTeam11/src/');
sys.path.insert(0,'..');
import src
from src import Rivet
from src import FinalDataPattern

class PruneSampleAnalysis:
    def __init__(self):
        self.hi = "hi"

    def printDirFiles(self, directory):
        onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
        fileMatches = []

        for f in onlyfiles:
            currFileMatches = []
            for i in range(1, 3):
                print("PruneSampleAnalysis - File:" + str(f) + " Samplepct:" + str((float(i)/30.0)))
                rivet = Rivet(0, (float(i)/30.0), str("/" + directory + "/" + f))
                print("PruneSampleAnalysis - Generating RPL")
                rivet.runGenerator()
                print("PruneSampleAnalysis - Getting match percent")
                fdp = FinalDataPattern(str("/" + directory + "/" + f), "auto.rpl", "auto")
                fdp.runCustomizedPattern()
                

                currFileMatches.append(fdp.getMatchPct())
            fileMatches.append(currFileMatches)
        handles = []
        for entry, m in enumerate(fileMatches):
            plt.plot(range(1, 3), m, label=str(onlyfiles[entry]))
            plt.title('match percentage vs sample percentage')
            plt.ylabel('match percentage')
            plt.xlabel('sample pct')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    inputDirectory = ""
    try:
        options, remainder = getopt.getopt(sys.argv[1:], '', ['test'])
    except getopt.GetoptError as err:
        print err
        sys.exit(0)
    for opt, arg in options:
        if opt in ('test'):
            print "this was a test of the emergency alert system"
    numArgs = len(remainder)
    if numArgs == 0:
        print("No input file directory specified")
        exit(0)
    elif (numArgs == 1):
        if remainder[0].upper() == "HELP":
            print("Help Page")
        else:
            inputDirectory = remainder[0]
    analysis = PruneSampleAnalysis()
    analysis.printDirFiles(inputDirectory)

'''
	plt.plot([2,4,6,8,10], history.history['val_acc'])
	plt.title('model accuracy')
	plt.xlabel('hidden neurons')
	plt.ylabel('accuracy')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()
'''
