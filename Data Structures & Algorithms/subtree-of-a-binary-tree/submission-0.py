# NeetCode provides the TreeNode class.

class Solution:
    def isSubtree(self, root, subRoot):

        def isSameTree(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return (
                isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )

        if root is None:
            return False

        if isSameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )