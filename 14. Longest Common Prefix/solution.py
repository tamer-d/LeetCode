class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        smallest = min(strs)
        largest = max(strs)

        i = 0
        while i < len(smallest) and i < len(largest) and smallest[i] == largest[i]:
            i += 1

        return smallest[:i]
