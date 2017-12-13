"""
sample.py

sample.py randomply (and efficiently) selects lines from a specified input file, and outputs
them to a file under the /resource/ directory for use with BruteForce.py. This module does 
not require semistructured data, and can be used for other purpses outside of the Rivet system

Authors: James Baggs, Xiaoyu Chen, Yuxu Yang

(Program outputs sample files to /result/ directory and assumes datafiles are in /resource/)

Usage:      >python sample.py <samplePercentage> <inputFile>
Example:    >python sample.py 10 NewDataSet.csv

Output:     Outputs a file to the /resource/ directory in the project. The output
            is named "sample_<inputFilename>" which contains the same file extension
            as the input file.

"""

import os, json, sys
import random


class sample():
    def __init__(self, samplePercentage, inputfile):
        try:
            ############
            # GLOBAL VARS
            self.samplePercentage = samplePercentage
            self.inputfile = os.path.abspath(__file__+ "/../../") + "/resource/" + inputfile  ## Command line argument get file name from command line
            self.outputfile = os.path.abspath(__file__+ "/../../") + "/resource/" +  "sample_" + os.path.basename(inputfile)
        ############
        except IndexError as err:
            print("Required arguments: Sample size, input file, output file")
            print("eg: >python sample.py 5 Data.csv Output.csv")
            exit(0)

    def sampling(self):
        print("Start sampling...")
        num_lines = sum(1 for line in open(self.inputfile))

        size = int(num_lines * (float(self.samplePercentage) / 100.0))

        select_idx = random.sample(range(0, num_lines), size)

        filesize = os.path.getsize(self.inputfile)
        progress = 0
        f = open(self.outputfile, 'w')
        for i, line in enumerate(open(self.inputfile)):
            if i in select_idx:
                f.write(line)
            ## Progress bar
            progress = progress + len(line)
            progressPercent = round((float)(progress) / filesize * 100, 1)
            print '\r[{0}] {1}%'.format('#' * (int(progressPercent) / 2), progressPercent),
        f.close()
        print("")
        if (size == 0):
            print("Sample size is small")
            sys.exit(1)
        else:
            print("Sampling complete: ")
            print("Number of lines in input file: " + str(num_lines))
            print("Number of lines to sample: " + str(size))
            print("")

if __name__ == "__main__":
    sample = sample(sys.argv[1], sys.argv[2])
    sample.sampling()