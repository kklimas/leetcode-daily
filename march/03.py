class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    current_node = head
    length = 0
    while current_node is not None:
        length += 1
        current_node = current_node.next

    current_node = head
    subtracted_len = length - n

    if subtracted_len == 0:
        return head.next

    while subtracted_len > 1:
        subtracted_len -= 1
        current_node = current_node.next

    if current_node.next is not None:
        current_node.next = current_node.next.next
    else:
        current_node.next = None
    return head


def print_list(head):
    while head is not None:
        print(head.val)
        head = head.next

node = ListNode(2, ListNode(5, ListNode(8, ListNode(9))))
nodex = remove_nth_from_end(node, 1)
print_list(nodex)