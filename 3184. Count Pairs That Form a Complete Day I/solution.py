# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours):
        count = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1
        return count
