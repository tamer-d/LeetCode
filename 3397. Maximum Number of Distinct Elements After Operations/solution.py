# 3397. Maximum Number of Distinct Elements After Operations

class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        ans = 0
        pre = float('-inf')  

        for x in nums:
            low = x - k
            need = pre + 1
            # on veut au moins need et au moins low
            candidate = max(low, need)
            if candidate > x + k:
                continue
            ans += 1
            pre = candidate

        return ans