#!/usr/bin/env python


def calculate_fibonacci( number ):
    if number == 1  or number == 2:
        return 1
    return calculate_fibonacci(number - 1 ) + calculate_fibonacci( number - 2)

