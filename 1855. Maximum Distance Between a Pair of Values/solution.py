# solution.py
# 1855. Maximum Distance Between a Pair of Values

class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0
        j = 0
        ans = 0
        n1 = len(nums1)
        n2 = len(nums2)

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
