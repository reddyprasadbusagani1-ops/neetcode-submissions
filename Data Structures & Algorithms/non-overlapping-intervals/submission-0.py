
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                # Overlap: remove the interval that ends later
                removals += 1
                prev_end = min(prev_end, end)
            else:
                # No overlap: keep the current interval
                prev_end = end

        return removals
