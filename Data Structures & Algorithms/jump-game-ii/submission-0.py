
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest = 0

            # Find the farthest index reachable
            # from the current range
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            # Move to the next range
            left = right + 1
            right = farthest

            jumps += 1

        return jumps
