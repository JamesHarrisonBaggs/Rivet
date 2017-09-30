# coding: utf-8
#  -*- Mode: Python; -*-                                              
# 
#  brute-force-method.py
# 
#  ? Copyright IBM Corporation 2016, 2017.
#  LICENSE: MIT License (https://opensource.org/licenses/mit-license.html)
#  AUTHOR: Jamie A. Jennings

# Developed using MacOSX Python 2.7.10, cffi 1.7.0
# easy_install --user cffi

import os, json, sys
import rosie
import subprocess
import time

############
#GLOBAL VARS
try:
    programName = sys.argv[1]
    fileName = sys.argv[2]
    numTimingRuns = 5
except IndexError:
    print ("Two arguments are expected. the first for the program to time, and the second for the file to pass to the program.\n e.g. - 'python testTime.py testLoadJson.py output.json'")
    exit(-1)
############


# For each timing run, open a subprocess, time the execution of the command, capture the timing output, and average the number of times.
realtimes = []
for x in range(0,numTimingRuns):
    #Create the subprocess. Pipe the stdout into p.
    p = subprocess.Popen("/usr/bin/time" + " -p python " + programName + " " + fileName , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    #While there is output to read, read it. Append "real" times to realtimes[].
    while True:
        line = p.stdout.readline()
        if "real" in line:
            realtimes.append(line[5:])
        if line == '' and p.poll() != None:
            break

#Print the times, and print their average.
totaltime = 0
for idx, inputs in enumerate(realtimes):
    print "time " + str(idx) + ":",
    print inputs,
    totaltime += float(inputs)
print "average times: " + str(totaltime/5)



    

