# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks):
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1

        rounds = 0
        for freq in counts.values():
            if freq == 1:
                return -1
            rounds += freq // 3
            if freq % 3 != 0:
                rounds += 1
        return rounds