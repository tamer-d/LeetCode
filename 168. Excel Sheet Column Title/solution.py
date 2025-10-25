# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1 
            char = chr(ord('A') + (columnNumber % 26))
            result = char + result
            columnNumber //= 26
        return result
