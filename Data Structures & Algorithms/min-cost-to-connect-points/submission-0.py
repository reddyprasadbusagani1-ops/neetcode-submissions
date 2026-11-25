class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                distance = (
                    abs(points[i][0] - points[j][0]) +
                    abs(points[i][1] - points[j][1])
                )
                edges.append((distance, i, j))

        edges.sort()

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost
                edges_used += 1

                if edges_used == n - 1:
                    break

        return total_cost