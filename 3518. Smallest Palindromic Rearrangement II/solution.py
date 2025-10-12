class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        half = []
        mid = ""
        for ch in sorted(freq.keys()):
            cnt = freq[ch]
            half.extend([ch] * (cnt // 2))
            if cnt % 2 == 1:
                mid = ch  

        perms = []
        used = [False] * len(half)

        half_chars = half

        def backtrack(path):
            if len(path) == len(half_chars):
                perms.append("".join(path))
                return
            prev = None
            for i in range(len(half_chars)):
                if used[i]:
                    continue
                if prev is not None and half_chars[i] == prev:
                    continue
                used[i] = True
                path.append(half_chars[i])
                backtrack(path)
                path.pop()
                used[i] = False
                prev = half_chars[i]

        backtrack([])

        # trier les permutations distinctes
        perms = sorted(set(perms))

        if k > len(perms):
            return ""

        chosen = perms[k - 1]

        left = chosen
        right = left[::-1]
        if len(s) % 2 == 1:
            return left + mid + right
        else:
            return left + right
