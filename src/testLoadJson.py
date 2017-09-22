# coding: utf-8
#  -*- Mode: Python; -*-                                              
# 
#  brute-force-method.py
# 
#  � Copyright IBM Corporation 2016, 2017.
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

##Use the basic.matchall to parse all data
with open(filename) as file: ## Data file need to analyize 
    data = json.load(file)
    data = data['basic.matchall']['subs'][0]
#     if 'subs' in data:1
#     data = data['subs']
    
    print data.keys()

#     while (data != None):
#         data = data
            # print number            

# print "A message should print below, as the program exits, indicating that engine", engine.id, "is being collected"