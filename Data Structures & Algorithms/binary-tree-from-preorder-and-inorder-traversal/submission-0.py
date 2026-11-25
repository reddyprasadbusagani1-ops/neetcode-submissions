# NeetCode provides the TreeNode class.

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {
            value: index for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def dfs(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            # First element in preorder is the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find root position in inorder
            mid = inorder_map[root_value]

            # Build left and right subtrees
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)