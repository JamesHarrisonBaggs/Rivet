#  BruteForce.py
# 
#  A program that uses Rosie's "match all" functionality
#  to match parsed data against Rosie's library of patterns.
# 
#  Code copied and modified from rtest.py.
#
#  Authors: Xiaoyu Chen, James Baggs, Yuxu Yang, Colleen Britt

import os, json, sys
import rosie

class BruteForce:
    
    def __init__(self, filename):
        """Save the file name given from command-line."""
        self.filename = filename
    
    def runBrute(self):
        """Runs the program."""
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

        list = []

        def print_match_results(r, of):
            match = json.loads(r[0]) if r else False
            if match:
                ## This part was modified to write output into a json file instead of std output
                list.append(match)
                leftover = json.loads(r[1])
            else:
                print "Match failed."

        ##Use the basic.matchall to parse all data
        config = json.dumps( {'expression': 'basic.matchall'} )
        r = engine.configure(config)
        number = 0
        with open(self.filename) as file: ## Data file need to analyize 
            with open("output.json", 'w') as of: ## This is the output json file that contains all pattern that matched
                for line in file:
                    r = engine.match(line, None)
                    print_match_results(r, of)
                    # list.append(result)
                    number += 1 ## This is just keep tracking lines numbers
                    # print number            
                json.dump(list, of, indent = 2)

if __name__ == "__main__":
  brute = BruteForce(sys.argv[1])
  brute.runBrute()