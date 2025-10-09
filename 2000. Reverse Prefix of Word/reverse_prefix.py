# LeetCode Problem: 2000. Reverse Prefix of Word
# Link: https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word, ch):
        i = 0
        while i < len(word) and word[i] != ch:
            i += 1

        if i == len(word):
            return word

        prefix_reversed = word[:i+1][::-1]
        return prefix_reversed + word[i+1:]
