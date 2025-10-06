# LeetCode Problem: 778. Swim in Rising Water
# Link: https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def canReach(t):
            visited = [[False] * n for _ in range(n)]
            
            def dfs(x, y):
                if x == n - 1 and y == n - 1:
                    return True
                visited[x][y] = True
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n and 0 <= ny < n and 
                        not visited[nx][ny] and 
                        grid[nx][ny] <= t
                    ):
                        if dfs(nx, ny):
                            return True
                return False

            if grid[0][0] > t:
                return False
            return dfs(0, 0)

        left, right = grid[0][0], n * n - 1
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
