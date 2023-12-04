#!/usr/bin/python3
"""
    Lockboxes Tasks
"""


def canUnlockAll(boxes):
    """
        Return true if all boxes in the array can opened
    """
    # check if boxes is empty
    if len(boxes) == 0:
        return False

    unlocked = set()
    unlocked.add(0)

    for idx, val in enumerate(boxes):
        # check if index box can't be unlocked
        if idx not in unlocked:
            return False

        # add key indexes from unlocked box
        for ele in val:
            # check each ele index and update the set
            if ele < len(boxes) and ele > idx:
                unlocked.update(boxes[ele])
        unlocked.update(val)

    return True
