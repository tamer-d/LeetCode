class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()  
        min_diff = 10**9  
        
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff
