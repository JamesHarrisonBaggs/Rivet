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
from Patterns import Patterns
from platform import node

############
#GLOBAL VARS
filename = sys.argv[1]
############

root = Patterns("Root")
current = root

## This function is save to print all pattern name
# def parseLineR(jsonData):
#     if 'subs' not in jsonData.values()[0]:
#         strKey = json.dumps(jsonData.keys())
#         result = strKey.split('\"')[1].strip()
#         print result
#     else: 
#         data = jsonData.values()[0]['subs']
#         for i in range(len(data)):
#             sub = data[i]
#             parseLineR(sub)

## Extract all pattern name from the json file
## create pattern object and store them in a tree.
def parseLine(jsonData):
    global current
    global root
    if 'subs' not in jsonData.values()[0]:
        strKey = json.dumps(jsonData.keys())
        result = strKey.split('\"')[1].strip()
        node = Patterns(result)
        nextIndex = current.isInList(node)
        # Check if this pattern is already exist in the tree
        if(nextIndex >= 0):
            current = current.next[nextIndex]
            current.count += 1
        else:
            nextIndex = current.addNode(node)
            current = current.next[nextIndex]
            current.count += 1
    else: 
        data = jsonData.values()[0]['subs']
        for i in range(len(data)):
            sub = data[i]
            parseLine(sub)

##Use the basic.matchall to parse all data
with open(filename) as file: ## Data file need to analyize 
    data = json.load(file)
    for i in range(len(data)):
        parseLine(data[i])
        current = root
## below are the code use to print all patterns
#         parseLineR(data[i])
#         print "line end here ----------------------------------------------"
#         print i


## This function print each level of the tree.
def printPatter(node):
    currlvl = list()
    currlvl.append(node)
    nextlvl = list()
    while currlvl:
        for i in range(len(currlvl)):
                for j in range(len(currlvl[i].next)):
                    nextlvl.append(currlvl[i].next[j])
        
        for i in range(len(currlvl)):
            print currlvl[i].name, currlvl[i].count, 
        print ""
        currlvl = nextlvl
        nextlvl = []
       
printPatter(root)