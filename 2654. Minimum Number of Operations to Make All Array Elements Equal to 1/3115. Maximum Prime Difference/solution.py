# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return -1 if min_len == float('inf') else (min_len - 1) + (n - 1)
