# coding: utf-8
#  -*- Mode: Python; -*-
#
#
#
#  Accepts arguments for DataFile, FilePattern
#  Accepts Option --timingRuns=<x> for number of timing runs. (alternatively "-t <x>" works)
#  Times Rosie's Data Extraction of DataFile by Brute force, and compares
#     to Rosie's Data Extraction of DataFile by FilePattern.
#  Defaults: 1 timing run
#  Defaults: BruteForce only if no FilePattern specified
#  Example: $>python ExtractionTime.py --timingRuns=5 UniformGeneratedData.csv FilePattern.rpl

'''
This program's basic functionality is complete, though some potentially needed changes are:
Update Subprocess call (line 69) to be compatible with rosie1.0
Return a Pass/Fail to command line based off of BruteForce/FilePattern speed (rather than just the speeds themselves)
Measure standard deviation / z-score of timing runs, rather than just the average
'''
#
#  ? Copyright IBM Corporation 2016, 2017.
#  LICENSE: MIT License (https://opensource.org/licenses/mit-license.html)
#  AUTHOR: JHBaggs
#  PYTHON: 2.7.12



import os, json, sys
import subprocess
import time
import getopt
import timeit
import os.path
sys.path.insert(0,'..');
import src
from src import BruteForce
from src import FinalDataPattern

############
# GLOBAL VARS
bruteForceOnly = False
numTimingRuns = 5
dataFileName = ''
filePatternName = ''
############

############
# Argument/Option parser
options, remainder = getopt.getopt(sys.argv[1:], 't:', ['timingRuns='])

for opt, arg in options:
    if opt in ('-t', '--timingRuns'):
        numTimingRuns = int(arg)
        print("Running " + str(numTimingRuns) + " data extractions by both BruteForce and RPL")
if (len(remainder) == 3):
    dataFileName = remainder[0]
    filePatternName = remainder[1]
    pattern = remainder[2]
elif ((len(remainder) != 1)):
    print("Requires 1 or 3 Arguments: DataFile(required), FilePattern.rpl(optional), PatternName")
else:
    bruteForceOnly = True
    print("Brute Force Only Mode.")
    dataFileName = remainder[0]

if (".rpl" not in filePatternName and not bruteForceOnly):
    print("File pattern must be a .rpl file")
    exit(-1)

# End Argument Parser

############
# Brute force run timer


# For each timing run, open a subprocess, time the execution of the command, capture the timing output, and average the number of times.
realtimes = []
totaltime = 0
print
print("*Begin Brute Force Timing Runs (These may take a long time for large files)*")
for x in range(0, numTimingRuns):
    # Create the subprocess. Pipe the stdout into p.

    start_time = timeit.default_timer()

    dataParser = BruteForce( os.path.basename(os.path.normpath(dataFileName)))
    data = dataParser.runBrute()

    elapsed = timeit.default_timer() - start_time
    print("trial #" + str(x) + ": " + str(round(elapsed,2)) + " seconds")
    realtimes.append(elapsed)
    totaltime = totaltime+elapsed
'''
    # While there is output to read, read it. Append "real" times to realtimes[].
    while True:
        line = p.stdout.readline()
        if "real" in line:
            realtime = line[5:-1]
            print "time " + str(x) + ": " + realtime
            realtimes.append(realtime)
            totaltime += float(realtime)
        if line == '' and p.poll() != None:
            break
'''

avgBruteForceTime = totaltime / numTimingRuns

# end brute force run timer
############

############
# File Pattern Data Extraction Timer

if (bruteForceOnly):
    exit(0)

# For each timing run, open a subprocess, time the execution of the command, capture the timing output, and average the number of times.
realtimes = []
totaltime = 0
print
print("*Begin File Pattern Enhanced Timing Runs")
print filePatternName
FinalDataParser = FinalDataPattern( os.path.basename(os.path.normpath(dataFileName)), os.path.normpath(filePatternName), pattern)

for x in range(0, numTimingRuns):
    # While there is output to read, read it. Append "real" times to realtimes[].
    start_time = timeit.default_timer()

    FinalDataParser.runCustomizedPattern()

    elapsed = timeit.default_timer() - start_time
    print("trial #" + str(x) + ": " + str(round(elapsed,2)) + " seconds")
    realtimes.append(elapsed)
    totaltime = totaltime+elapsed

print "average RPL time: " + str(round((totaltime / numTimingRuns),2))
print "average brute force time: " + str(round(avgBruteForceTime,2))

# end rpl force run timer
############


