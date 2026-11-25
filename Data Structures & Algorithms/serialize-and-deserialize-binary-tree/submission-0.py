class Codec:

    def serialize(self, root):
        values = []

        def dfs(node):
            if node is None:
                values.append("#")
                return

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            value = next(values)

            if value == "#":
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()