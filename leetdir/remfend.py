from linked_list import ListNode

def remfend(head, n):
    slow_ptr = fast_ptr = head

    for _ in range(n):
        fast_ptr = fast_ptr.next

    while fast_ptr is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    slow_ptr.next = slow_ptr.next.next

    return head
