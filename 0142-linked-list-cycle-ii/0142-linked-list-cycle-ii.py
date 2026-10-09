class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Cycle detect karo
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Cycle ka starting node find karo
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow