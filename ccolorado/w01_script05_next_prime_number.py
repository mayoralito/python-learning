#!/usr/bin/env python
import sys

def is_prime( number ):
    for i in range( 2, number ):
        if number % i == 0 :
            return False
    return True

def next_prime( number ):
    prime = number + 1
    while(not is_prime( prime) ):
        prime += 1

    return prime

number = int(sys.argv[1])
if not isinstance( number, int):
  sys.exit(1)

print "The next prime number from %d is %d" % (number, next_prime(number))



