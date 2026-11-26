
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []

        for start, end in intervals:
            # No overlap: add a new interval
            if not result or result[-1][1] < start:
                result.append([start, end])

            # Overlap: merge intervals
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
