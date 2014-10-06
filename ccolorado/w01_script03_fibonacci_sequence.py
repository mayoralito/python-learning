#!/usr/bin/env python
import sys

def calculate_fibonacci( number ):
    if number == 1  or number == 2:
        return 1
    return calculate_fibonacci(number - 1 ) + calculate_fibonacci( number - 2)


number = int(sys.argv[1])
if not isinstance( number, int):
  sys.exit(1)

series = []
for n in range (1, number):
  series.append( calculate_fibonacci(n) )

print series
