# LeetCode Problem: 15. 3Sum
# Link: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(triplet) for triplet in result]
