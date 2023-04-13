#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """ can unlock all boxes"""
    n = len(boxes)
    visited = set([0])
    keys = set(boxes[0])

    while len(keys) > 0:
        key = keys.pop()
        if key < n and key not in visited:
            visited.add(key)
            keys.update(boxes[key])

    return len(visited) == n
