from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)

        for airport in adj:
            adj[airport].sort(reverse=True)

        itinerary = []

        def dfs(airport):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]