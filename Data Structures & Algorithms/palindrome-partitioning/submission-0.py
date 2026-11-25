class Solution:
    def partition(self, s):
        result = []
        current = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            # All characters are partitioned
            if start == len(s):
                result.append(current.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return result