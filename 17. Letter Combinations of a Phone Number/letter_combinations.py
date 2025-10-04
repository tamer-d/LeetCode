# LeetCode Problem: 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def helper(digits):
            if len(digits) == 1:
                return list(phone[digits[0]])

            rest_combinations = helper(digits[1:])
            result = []
            for char in phone[digits[0]]:
                for comb in rest_combinations:
                    result.append(char + comb)
            return result

        return helper(digits)
