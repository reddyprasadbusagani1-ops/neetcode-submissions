# NeetCode provides the ListNode class.

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Step 1: Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            # Step 2: Save the next group's starting node
            group_next = kth.next

            # Step 3: Reverse the current group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Step 4: Connect the reversed group
            old_group_start = group_prev.next

            group_prev.next = kth
            group_prev = old_group_start