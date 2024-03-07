class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head) -> bool:
        while head is not None:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
