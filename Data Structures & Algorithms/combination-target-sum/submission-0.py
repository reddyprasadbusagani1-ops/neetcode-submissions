class Solution:
    def combinationSum(self, nums, target):
        result = []
        current = []

        def backtrack(index, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target or index == len(nums):
                return

            # Include the current number (can reuse it)
            current.append(nums[index])
            backtrack(index, total + nums[index])

            # Backtrack
            current.pop()

            # Skip the current number
            backtrack(index + 1, total)

        backtrack(0, 0)
        return result