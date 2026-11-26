
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        directions = [
            (0, 1),   # Right
            (0, -1),  # Left
            (1, 0),   # Down
            (-1, 0)   # Up
        ]

        def dfs(r, c):
            # Return cached result
            if dp[r][c] != 0:
                return dp[r][c]

            # Path containing the current cell
            dp[r][c] = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries and increasing condition
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):

                    dp[r][c] = max(
                        dp[r][c],
                        1 + dfs(nr, nc)
                    )

            return dp[r][c]

        result = 0

        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))

        return result
