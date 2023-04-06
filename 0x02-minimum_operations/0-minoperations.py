#!/usr/bin/env python3
""" Minimum Operations """
def minOperations(n):
    """ min opreation """
    if n < 1:
        return 0
    elif n == 1:
        return 0
    else:
        clipboard = 1
        operations = 1 + minOperations(n-1)
        for i in range(2, n):
            if n % i == 0:
                operations = min(operations, i * minOperations(n//i) + i - 1)
        return operations
