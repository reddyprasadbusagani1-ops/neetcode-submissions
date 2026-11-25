class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(houses):
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )