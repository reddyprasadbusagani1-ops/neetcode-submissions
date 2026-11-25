class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # Move to i + 1 because each element can be used once
                backtrack(i + 1, remaining - candidates[i])

                current.pop()

        backtrack(0, target)
        return result