class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Calculate sum without carry
            sum_without_carry = (a ^ b) & MASK

            # Calculate carry
            carry = ((a & b) << 1) & MASK

            a = sum_without_carry
            b = carry

        # Convert 32-bit unsigned result to signed integer
        if a <= MAX_INT:
            return a
        return ~(a ^ MASK)