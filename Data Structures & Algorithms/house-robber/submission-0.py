class Solution:
    def rob(self, nums):
        n = len(nums)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            rob_current = nums[i] + dp[i + 2] if i + 2 <= n else nums[i]
            skip_current = dp[i + 1]

            dp[i] = max(rob_current, skip_current)

        return dp[0]