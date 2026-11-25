class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        return [num for num, freq in sorted(
            count.items(), key=lambda x: x[1], reverse=True
        )[:k]]
        