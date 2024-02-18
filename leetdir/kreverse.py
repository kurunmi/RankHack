from linked_list import ListNode
def reverseKGroup(head, k):
    count = 0
    ptr = head
    while ptr is not None:
        count += 1
        ptr = ptr.next

    if count < k:
        return head

    loops = count // k

    prev = dummy = ListNode(0, head)
    ptr = prev.next

    for loop in range(loops):
        for _ in range(k - 1):
            next_node = ptr.next
            ptr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        prev = ptr
        ptr = ptr.next
    return dummy.next





