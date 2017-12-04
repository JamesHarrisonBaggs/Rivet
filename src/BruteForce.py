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
from progressbar import ProgressBar

class BruteForce:
    
    def __init__(self, filename):
        """Initialize the variables."""
        self.filename = os.path.abspath(__file__+ "/../../") + "/resource/" +filename
        self.ROSIE_HOME = None
        self.Rosie = None
        self.engine = None
        self.config = None
        self.r = None
        self.tbl = None
        self.of = None
        self.list = []
        self.outputfile = os.path.abspath(__file__+ "/../../") + "/result/output.json"
        self.pbar = ProgressBar()
    
    def runBrute(self):
        print ("Parsing the data:...")
        """Runs the program."""
        self.ROSIE_HOME = os.getenv("ROSIE_HOME")
        if not self.ROSIE_HOME:
            print "Environment variable ROSIE_HOME not set.  (Must be set to the root of the rosie directory.)"
            sys.exit(-1)

        self.Rosie = rosie.initialize(self.ROSIE_HOME, self.ROSIE_HOME + "/ffi/librosie/librosie.so")
        # print "Rosie library successfully loaded"

        self.engine = self.Rosie.engine()
        # print "Obtained a rosie matching engine:", self.engine, "with id", self.engine.id

        self.config = json.dumps( {'encode': 'json'} )
        self.r = self.engine.configure(self.config)
        # if not self.r: print "Engine reconfigured to look for digits\n"
        # else: print "Error reconfiguring engine!", r

        self.r = self.engine.inspect()
        # print self.r

        self.tbl = json.loads(self.r[0])
        # print "Return from inspect_engine is:", str(self.tbl)

        self.r = self.engine.load_manifest("$sys/MANIFEST")
        # for s in self.r: print s

        
        ##Use the basic.matchall to parse all data
        self.config = json.dumps( {'expression': 'basic.matchall'} )
        self.r = self.engine.configure(self.config)
        number = 0
        with open(self.filename) as file: ## Data file need to analyize 
            with open(self.outputfile, 'w') as self.of: ## This is the output json file that contains all pattern that matched
                ## Variable for progress bar
                filesize = os.path.getsize(self.filename)
                progress = 0
                for line in file:
                    self.r = self.engine.match(line, None)
                    self.print_match_results(self.r, self.of)
                    number += 1 ## This is just keep tracking lines numbers      
                    
                    ## Progress bar
                    progress = progress + len(line)
                    progressPercent =  round((float)(progress) / filesize * 100, 1)
                    print '\r[{0}] {1}%'.format('#'*(int(progressPercent)/2), progressPercent),
                print("\nGenerating JSON output...")
                json.dump(self.list, self.of, indent = 2)
        print("\rParsing the data: Complete")
        print("")
        return self.list

    def print_match_results(self, r, of):
        match = json.loads(r[0]) if r else False
        self.list.append(match)
        leftover = json.loads(r[1])

if __name__ == "__main__":
    Brute = BruteForce(sys.argv[1])
    Brute.runBrute()
