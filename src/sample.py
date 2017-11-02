"""
    A program reads a sample datafile and outputs a sample
    of the lines of that file

"""

import os, json, sys
# import pandas as pd
import random

class sample():

	def __init__(self, samplePercentage, inputfile):
		try:
			############
			#GLOBAL VARS
			self.samplePercentage = samplePercentage
			self.inputfile = inputfile ## Command line argument get file name from command line
			self.outputfile = inputfile + "_sample"
			############
		except IndexError as err:
			print("Required arguments: Sample size, input file, output file")
			print("eg: >python sample.py 5 Data.csv Output.csv")
			exit(0)
	def sampling(self):
		num_lines = sum(1 for line in open(self.inputfile))

		size = int(num_lines * ((self.samplePercentage)/100.0))

		select_idx = random.sample(range(0, num_lines), size)

		f = open(self.outputfile, 'w')
		for i, line in enumerate(open(self.inputfile)):
		    if i in select_idx:
		    	f.write(line)   
		f.close()
		if(size == 0):
			print("Sample size is small")
			sys.exit(1)
		else:
			print("Sampling complete: ")
			print("Number of lines in input file: " + str(num_lines))
			print("Number of lines to sample: " +str(size))
			print("")