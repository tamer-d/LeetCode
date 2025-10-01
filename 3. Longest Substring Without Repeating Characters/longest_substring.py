# LeetCode Problem: 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0
        best_substring = ""

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right

            # calcul longueur actuelle
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                best_substring = s[left:right+1]

        print("Sous-chaîne trouvée :", best_substring)
        print("Longueur :", max_length)

        return max_length
