class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * n
        visited = set([start])
        result = [start]

        total = k ** n  

        def dfs():
            if len(visited) == total:
                return True

            prefix = result[-1][1:]  

            for d in range(k):
                new = prefix + str(d)
                if new not in visited:
                    visited.add(new)
                    result.append(new)
                    if dfs():
                        return True
                    visited.remove(new)
                    result.pop()

            return False

        dfs()
        ans = result[0]
        for s in result[1:]:
            ans += s[-1]
        return ans
