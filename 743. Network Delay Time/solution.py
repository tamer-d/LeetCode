# 743. Network Delay Time

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        visited = set()

        while len(visited) < n:
            cur_node = None
            cur_dist = float('inf')
            for node in range(1, n + 1):
                if node not in visited and dist[node] < cur_dist:
                    cur_dist = dist[node]
                    cur_node = node

            if cur_node is None:
                break  

            visited.add(cur_node)

            for neighbor, weight in graph[cur_node]:
                if dist[cur_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[cur_node] + weight

        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1
