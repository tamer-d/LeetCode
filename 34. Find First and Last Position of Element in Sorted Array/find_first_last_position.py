# LeetCode Problem: 34. Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first, last = -1, -1

        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i      
        return [first, last]
