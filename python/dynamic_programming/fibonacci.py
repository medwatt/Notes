#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By   : medwatt
# Description  : Calculating the nth Fibonacci number
# =============================================================================
from time_it import timed

### Brute-Force
@timed
def fib_0(n):

    def helper(n):
        if n <= 2:
            return 1
        else:
            return helper(n - 1) + helper(n - 2)

    return helper(n)


### Memoized
@timed
def fib_1(n):
    memo = {0: 0, 1: 1}

    def helper(n):
        if n not in memo:
            memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)


### Tabulation
@timed
def fib_2(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[-1] += table[-2]
    return table[-1]

if __name__ == "__main__":
    # input
    n = 30
    # print result
    print("Brute Force:\tres = {}, time = {}".format(*fib_0(n)))
    print("Memorized:\tres = {}, time = {}".format(*fib_1(n)))
    print("Tabular:\tres = {}, time = {}".format(*fib_2(n)))
