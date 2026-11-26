
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1

            half = power(x, n // 2)
            result = half * half

            if n % 2 == 1:
                result *= x

            return result

        result = power(x, abs(n))

        if n < 0:
            return 1 / result

        return result
