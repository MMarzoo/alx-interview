#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n):
    ''' execute only two operations in this file '''
    if not isinstance(n, int):
        return 0

    operation = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operation += iterator
            iterator = 1
        iterator += 1
    return operation
