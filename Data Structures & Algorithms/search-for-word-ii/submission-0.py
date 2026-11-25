class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            current = root

            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()

                current = current.children[char]

            current.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            # Check whether character exists in Trie
            if char not in node.children:
                return

            next_node = node.children[char]

            # Word found
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark current cell as visited
            board[r][c] = "#"

            # Explore four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):
                    dfs(nr, nc, next_node)

            # Restore original character
            board[r][c] = char

            # Trie pruning: remove exhausted branches
            if not next_node.children and next_node.word is None:
                del node.children[char]

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result