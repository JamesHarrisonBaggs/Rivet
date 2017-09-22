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

ROSIE_HOME = os.getenv("ROSIE_HOME")
if not ROSIE_HOME:
    print "Environment variable ROSIE_HOME not set.  (Must be set to the root of the rosie directory.)"
    sys.exit(-1)

Rosie = rosie.initialize(ROSIE_HOME, ROSIE_HOME + "/ffi/librosie/librosie.so")
print "Rosie library successfully loaded"

engine = Rosie.engine()
print "Obtained a rosie matching engine:", engine, "with id", engine.id

config = json.dumps( {'encode': 'json'} )
r = engine.configure(config)
if not r: print "Engine reconfigured to look for digits\n"
else: print "Error reconfiguring engine!", r

r = engine.inspect()
print r

tbl = json.loads(r[0])
print "Return from inspect_engine is:", str(tbl)

r = engine.load_manifest("$sys/MANIFEST")
for s in r: print s

def print_match_results(r, of):
    match = json.loads(r[0]) if r else False
    if match:
        ## This part was modified to write output into a json file 
        ## instead of std output
        json.dump(match, of, indent = 2) 
        ####print "Match succeeded!" 
        ####print "Match structure is", match
        leftover = json.loads(r[1])
        # print "And there were", leftover, "unmatched characters"
    else:
        print "Match failed."

##Use the basic.matchall to parse all data
config = json.dumps( {'expression': 'basic.matchall'} )
r = engine.configure(config)
number = 0
with open(filename) as file: ## Data file need to analyize 
    with open("output.json", 'w') as of: ## This is the output json file that contains all pattern that matched
        for line in file:
            r = engine.match(line, None)
            print_match_results(r, of)
            number += 1 ## This is just keep tracking lines numbers
            # print number            

# print "A message should print below, as the program exits, indicating that engine", engine.id, "is being collected"