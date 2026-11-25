from collections import defaultdict

class Solution:
    def foreignDictionary(self, words):
        adj = defaultdict(set)
        chars = set()

        for word in words:
            for char in word:
                chars.add(char)
                adj[char]

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            visited[char] = False
            result.append(char)

            return False

        for char in chars:
            if char not in visited:
                if dfs(char):
                    return ""

        return "".join(result[::-1])