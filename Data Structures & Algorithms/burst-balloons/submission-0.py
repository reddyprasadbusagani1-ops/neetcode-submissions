
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary balloons with value 1
        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        def dfs(left, right):
            # No balloons remaining
            if left > right:
                return 0

            # Return cached result
            if dp[left][right] != -1:
                return dp[left][right]

            result = 0

            # Choose the last balloon to burst
            for i in range(left, right + 1):

                coins = (
                    nums[left - 1] * nums[i] * nums[right + 1]
                    + dfs(left, i - 1)
                    + dfs(i + 1, right)
                )

                result = max(result, coins)

            dp[left][right] = result

            return result

        return dfs(1, n - 2)
