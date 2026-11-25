# NeetCode provides the Node class.

class Solution:
    def copyRandomList(self, head):
        old_to_new = {None: None}

        # Step 1: Create a copy of every node
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random pointers
        current = head

        while current:
            copy = old_to_new[current]

            copy.next = old_to_new[current.next]
            copy.random = old_to_new[current.random]

            current = current.next

        return old_to_new[head]