import getopt
import sys
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
from Rivet import Rivet


class PruneSampleAnalysis:
    def __init__(self):
        self.hi = "hi"

    def printDirFiles(self, directory):
        onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
        fileMatches = []

        for f in onlyfiles:
            currFileMatches = []
            for i in range(1, 3):
                rivet = Rivet(0, float(i) / 30, str("./" + directory + "/" + f))
                currFileMatches.append(rivet.getMatchPct())
            fileMatches.append(currFileMatches)
        for m in fileMatches:
            plt.plot(range(1, 3), m)
            plt.title('match percentage vs sample percentage')
            plt.ylabel('match percentage')
            plt.xlabel('sample pct')
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
