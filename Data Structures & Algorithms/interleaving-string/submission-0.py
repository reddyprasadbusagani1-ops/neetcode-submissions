
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        # Length check
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty strings can form an empty string
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0 and j == 0:
                    continue

                k = i + j - 1

                # Take the character from s1
                if i > 0 and s1[i - 1] == s3[k]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                # Take the character from s2
                if j > 0 and s2[j - 1] == s3[k]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[m][n]
