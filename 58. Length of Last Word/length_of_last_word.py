# LeetCode Problem: 58. Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])