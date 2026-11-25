# NeetCode provides the TreeNode class.

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return diameter