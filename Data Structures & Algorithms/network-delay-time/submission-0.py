import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in dist:
                continue

            dist[node] = time

            for neighbor, weight in adj[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())