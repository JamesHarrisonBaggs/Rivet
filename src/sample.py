import pandas as pd
import random, sys

# The data to load
f = sys.argv[1]

# Count the lines
num_lines = sum(1 for l in open(f))

# Sample size - in this case ~20%
size = int(num_lines / 5)

# The row indices to skip - make sure 0 is not included to keep the header!
skip_idx = random.sample(range(0, num_lines), num_lines - size)

# Read the data
data = pd.read_csv(f, skiprows=skip_idx)
# print data

data.to_csv('sample.csv', index=False)