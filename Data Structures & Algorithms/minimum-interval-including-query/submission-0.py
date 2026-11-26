
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [-1] * len(queries)
        heap = []

        i = 0

        for q, index in sorted_queries:

            # Add all intervals that start before or at q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1

            # Remove intervals that end before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest valid interval is at the top
            if heap:
                result[index] = heap[0][0]

        return result
