#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ min opreation """
    if n < 1:
        return 0
    elif n == 1:
        return 0
    else:
        operations: int = 1 + minOperations(n-1)
        for i in range(2, n):
            if n % i == 0:
                operations = min(operations, i * minOperations(n//i) + i - 1)
        return operations
