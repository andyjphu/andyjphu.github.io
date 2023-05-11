from typing import List

def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

    minKey = 0
    out = 0
    for key, value in enumerate(nums1):
        for index, item in enumerate(nums2[minKey:]):
            if (item == value):
                minKey+=index 
                out+=1
    return out


try:
    assert maxUncrossedLines(None, [2,5,1,2,5], [10,5,2,1,5,2]) == 3
except AssertionError as e:
    print("issuie")
    print(e)