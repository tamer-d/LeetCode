from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)  
            
            sorted_freq = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            s = 0
            for j in range(min(x, len(sorted_freq))):
                val, _ = sorted_freq[j]
                s += val
                
            ans.append(s)
        
        return ans