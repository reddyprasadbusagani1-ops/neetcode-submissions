class Solution:
    def permute(self, nums):
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose the element
                current.append(nums[i])
                used[i] = True

                backtrack()

                # Backtrack
                current.pop()
                used[i] = False

        backtrack()
        return result