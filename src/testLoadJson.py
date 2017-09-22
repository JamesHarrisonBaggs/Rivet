# coding: utf-8
#  -*- Mode: Python; -*-                                              
# 
#  brute-force-method.py
# 
#  © Copyright IBM Corporation 2016, 2017.
#  LICENSE: MIT License (https://opensource.org/licenses/mit-license.html)
#  AUTHOR: Jamie A. Jennings

# Developed using MacOSX Python 2.7.10, cffi 1.7.0
# easy_install --user cffi

import os, json, sys
import rosie

############
#GLOBAL VARS
filename = sys.argv[1]
############

def parseLine(jsonData):
    if 'subs' not in jsonData.values()[0]:
        print jsonData.keys()
    else: 
        data = jsonData.values()[0]['subs']
        for i in range(len(data)):
            sub = data[i]
            parseLine(sub)

##Use the basic.matchall to parse all data
with open(filename) as file: ## Data file need to analyize 
    data = json.load(file)
    for i in range(len(data)):
        parseLine(data[1])
        print "line end here ----------------------------------------------"
        print i
