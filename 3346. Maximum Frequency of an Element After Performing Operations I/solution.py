# 3346. Maximum Frequency of an Element After Performing Operations I

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        l = 0

        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            window_size = r - l + 1
            ans = max(ans, min(window_size, numOperations + sum(1 for i in range(l, r + 1) if nums[i] == nums[r])))
        
        return ans
