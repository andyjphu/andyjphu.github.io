from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2+1)] * (n1 + 1) #TODO CONFIRM


        for i in range (1,n1 + 1):
            for j in range (1,n2 + 1):   
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])


        return dp[n1][n2]
        
    def maxUncrossedLines2(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]

nums1 = [3,2]
nums2 = [3,3,3]
'''
try:
    assert Solution.maxUncrossedLines(Solution, nums1, nums2 ) == 1
    print("good exit")
except AssertionError as e:
    print(e)
    print("bad exit")
'''
try: 
    n1 = len(nums1)
    n2 = len(nums2)
    arr1 = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    arr2 = [[0] * (n2+1)] * (n1 + 1)
    assert arr1 == arr2
    print(arr1)
    print(arr2)
except AssertionError as e:
    print(e)
    print("second assertion failed")