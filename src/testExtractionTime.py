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
#  Example: $>python testExtractionTime.py --timingRuns=5 UniformGeneratedData.csv FilePattern.rpl

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
import rosie
import subprocess
import time
import getopt

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
if (len(remainder) == 3):
    dataFileName = remainder[0]
    filePatternName = remainder[1]
    pattern = remainder[2]
elif ((len(remainder) != 1)):
    print("Requires 1 or 3 Arguments: DataFile(required), FilePattern.rpl(optional)")
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
    p = subprocess.Popen("/usr/bin/time" + " -p rosie basic.matchall " + dataFileName + " >/dev/null", shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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

bruteForceTime = totaltime / numTimingRuns

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
print("*Begin File Pattern Enhanced Timing Runs (These may take a long time for large files)*")
print filePatternName
rosieCommand = "/usr/bin/time" + " -p rosie -f " + filePatternName + " " + pattern + " " + dataFileName + " >/dev/null"
for x in range(0, numTimingRuns):
    # Create the subprocess. Pipe the stdout into p.
    p = subprocess.Popen(rosieCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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

print "average RPL time: " + str(totaltime / numTimingRuns)
print "average brute force time: " + str(bruteForceTime)

# end rpl force run timer
############


