from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        dq = deque()

        for i in range(len(nums)):

            # Remove indices outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding results once the window has size k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        