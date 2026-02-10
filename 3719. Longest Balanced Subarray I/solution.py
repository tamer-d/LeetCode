# 3719. Longest Balanced Subarray I

class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:   # paire
                    evens.add(nums[j])
                else:                 # impaire
                    odds.add(nums[j])
                if len(evens) == len(odds):
                    length = j - i + 1
                    if length > ans:
                        ans = length

        return ans
