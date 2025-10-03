# LeetCode Problem: 16. 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    if abs(total - target) < abs(closest_sum - target):
                        closest_sum = total

        return closest_sum
