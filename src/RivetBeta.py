import getopt
import sys
from sample import sample
from BruteForce import BruteForce
from PatternExtraction import PatternExtraction
from FinalRecognition import FinalRecognition



if __name__ == "__main__":
	try:
		options, remainder = getopt.getopt(sys.argv[1:], '', ['sampleSize='])
	except getopt.GetoptError as err:
	   		print err
	   		sys.exit(0)

	size = 5
	for opt, arg in options:
	    if opt in ('--sampleSize'):
	        size = arg
	numArgs = len(remainder)
	inputFile = ''
	# No input file
	if numArgs == 0:
	    print("No input file specified")
	    exit(0)
	elif(numArgs == 1):
	    if remainder[0].upper() == "HELP":
	        print("Help Page")
	    else:
	    	inputFile = remainder[0]

	## Modu
	sampler = sample(size, inputFile)
	sampler.sampling()

	dataParser = BruteForce(sampler.outputfile)
	dataParser.runBrute()

	extractor = PatternExtraction(dataParser.outputfile)
	extractor.runExtraction()

	rplGenerator = FinalRecognition(inputFile)
	rplGenerator.run()