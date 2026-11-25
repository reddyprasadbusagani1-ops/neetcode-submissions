# NeetCode provides the TreeNode class.

class Solution:
    def kthSmallest(self, root, k):
        count = 0
        result = 0

        def dfs(node):
            nonlocal count, result

            if node is None:
                return

            # Visit left subtree
            dfs(node.left)

            # Visit current node
            count += 1

            if count == k:
                result = node.val
                return

            # Visit right subtree
            dfs(node.right)

        dfs(root)
        return result