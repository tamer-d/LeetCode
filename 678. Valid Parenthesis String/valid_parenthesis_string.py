# LeetCode 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  
        high = 0 

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1  
                high += 1  

            if high < 0:  
                return False
            if low < 0: 
                low = 0

        return low == 0
