from typing import List


def extend_unique(list1: List, list2: List) -> List:
    """Helper function to mimic set behaviour on lists
    """
    res = list1
    for i in list2:
        if i not in res:
            res.append(i)
    return res