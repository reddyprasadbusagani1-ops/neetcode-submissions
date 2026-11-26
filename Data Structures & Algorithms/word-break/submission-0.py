class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in word_set:
                if s[i:i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break

        return dp[0]