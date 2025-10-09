# LeetCode 3494. Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution:
    def minTime(self, skill, mana):
        n = len(skill)  
        m = len(mana)   

        finish = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                time = skill[i] * mana[j]
                if i == 0 and j == 0:
                    finish[i][j] = time
                elif i == 0:
                    finish[i][j] = finish[i][j-1] + time
                elif j == 0:
                    finish[i][j] = finish[i-1][j] + time
                else:
                    finish[i][j] = max(finish[i-1][j], finish[i][j-1]) + time

        return finish[-1][-1]
