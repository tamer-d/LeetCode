# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums, key):
        freq = {}  
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                next_num = nums[i + 1]
                freq[next_num] = freq.get(next_num, 0) + 1


        most_common = -1
        max_count = 0
        for num, count in freq.items():
            if count > max_count:
                max_count = count
                most_common = num

        return most_common
