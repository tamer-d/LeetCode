class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = []
        smallest = s
        stack = [s]

        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.append(cur)

            if cur < smallest:
                smallest = cur

            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            rotated = cur[-b:] + cur[:-b]

            if added not in seen:
                stack.append(added)
            if rotated not in seen:
                stack.append(rotated)

        return smallest
