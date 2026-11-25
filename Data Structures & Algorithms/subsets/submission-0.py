class Solution:
    def subsets(self, nums):
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
                return

            # Include the current element
            subset.append(nums[index])
            backtrack(index + 1)

            # Exclude the current element
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result