"""
    A program reads a sample datafile and outputs a sample
    of the lines of that file

"""

import os, json, sys
import pandas as pd
import random

try:
	############
	#GLOBAL VARS
	samplePercentage = sys.argv[1]
	inputfile = sys.argv[2] ## Command line argument get file name from command line
	outputfile = sys.argv[3]
	############
except IndexError as err:
	print("Required arguments: Sample size, input file, output file")
	print("eg: >python sample.py 5 Data.csv Output.csv")
	exit(0)


num_lines = sum(1 for line in open(inputfile))
print("Number of lines in input file: " + str(num_lines))
size = int(num_lines * (int(samplePercentage)/100.0))
print("Number of lines to sample: " +str(size))

select_idx = random.sample(range(0, num_lines), size)

f = open(outputfile, 'w')
for i, line in enumerate(open(inputfile)):
    if i in select_idx:
    	f.write(line)   
f.close();