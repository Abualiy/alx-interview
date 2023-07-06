#!/usr/bin/pyhton3
"""
n number of locked boxes in front of you. Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
