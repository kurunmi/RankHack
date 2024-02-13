from linked_list import ListNode


def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    ptr = dummy = ListNode(0, head)

    for i in range(left):
        ptr = ptr.next
    current_node = ptr.next

    for i in range(right - left):
        next_node = current_node.next
        current_node.next, next_node.next, ptr.next = next_node.next, ptr.next, next_node
    return dummy






