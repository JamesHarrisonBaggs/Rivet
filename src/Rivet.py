"""
    This program extracts Rosie patterns from the specified input file
    and provides output options for both String and RPL types and to
    both console and .txt/.rpl files

    Author: JHBaggs
    Python Version 2.7.12

"""
import getopt
import sys

# Option/argument handler modified from https://pymotw.com/2/getopt/

'''
Options:
    --sampleSize=<Size>      ...     Number of lines to sample (Default 1)
    -r                       ...     Output as RPL (Defaults to String)
    -c                       ...     Print output to Console
    <input_filename / help>  ...     Filename to extract pattern from (Required) (or help output)
    <output_filename>        ...     Filename to print pattern to (Required if -o is specified)

Usage Examples: 
    python PatternExtractionR1.py -r -c inputfile.csv outputfile.rpl
        --> outputs RPL to .rpl file AND to console
    python PatternExtractionR1.py inputfile.csv outputfile.txt
        --> outputs String to .txt file

Code Example: 
#(-o, -h, -v, --output, --Verbose, and --version are all options. Options with ":" or "=" after them require arguments)
options, remainder = getopt.getopt(sys.argv[1:], 'o:hv', ['output=', 
                                                         'Verbose',
                                                         'version=',
                                                         ])
print 'OPTIONS   :', options

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
        output_filename = arg
    elif opt == '--version':
        version = arg
    elif opt in ('-h'):
        output_filename = 'help.txt'

print 'VERSION   :', version
print 'VERBOSE   :', verbose
print 'OUTPUT    :', output_filename
print 'REMAINING :', remainder
'''

# Prints an error message, syntax information and exits
def printHelp(message):
    print "****************************"
    print "*** " + message
    print "****************************"
    print
    print "Valid options are -r, -c, --debugTree and --sampleSize=<size>."
    print "\t-r prints RPL file instead of string pattern"
    print "\t-c also prints output to console"
    print "\t--debugTree prints the tree instead of rpl or txt file patterns\n"
    print "Syntax: '$python PatternExtractionR1.py <options> <inputfile> <outputfile>"
    print "Example: '$python PatternExtractionR1.py -r --sampleSize=10 Data.csv pattern3.rpl "
    print
    sys.exit(0)

# Options
sampleSize = 1
inputFile = ''
outputFile = ''
outputToConsole = False
outputRPL = False
debugTree = False

# Options/Remainder initialization (for scope purposes)
options = ''
remainder = ''

# Parse the options from command line
try:
    options, remainder = getopt.getopt(sys.argv[1:], 'rc', ['sampleSize=', 'debugTree'])
except getopt.GetoptError as err:
    printHelp("Invalid arguments")
    
# Assigns options from command line to variables
for opt, arg in options:
    if opt in ('-r'):
        outputRPL = True
    elif opt in ('-c'):
        outputToConsole = True
    elif opt == '--sampleSize':
        sampleSize = arg
    elif opt == '--debugTree':
        debugTree = True

# Error handling on incorrect arguments.
numArgs = len(remainder)

# No input file
if numArgs == 0:
    printHelp("No input file specified")

# No output file (or help specified)
elif(numArgs == 1):
    if remainder[0].upper() == "HELP":
        printHelp("Help Page")
    else:
        printHelp("No output file specified")

# Makes sure RPL output is to .rpl file
elif((numArgs == 2) and outputRPL):
    if ".rpl" not in remainder[1]:
        printHelp("Output file is not a .rpl file and -r is specified")

# Else: Everything is OK
else:
    inputFile = remainder[0]
    outputFile = remainder[1]
    

# Open files. If length inputFile < S




        



