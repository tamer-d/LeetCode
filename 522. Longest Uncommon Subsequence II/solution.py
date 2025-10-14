# 522. Longest Uncommon Subsequence II

class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        """Vérifie si 'a' est une sous-séquence de 'b'"""
        i = 0
        for c in b:
            if i < len(a) and a[i] == c:
                i += 1
        return i == len(a)

    def findLUSlength(self, strs: list[str]) -> int:
        strs.sort(key=len, reverse=True) 
        for i, s in enumerate(strs):
            if all(not self.isSubsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        return -1
