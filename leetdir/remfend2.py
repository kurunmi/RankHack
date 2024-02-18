from linked_list import ListNode

def remfend(head, n):
    ptr = prev = dummy = ListNode(0, head)
    count = 0

    while prev.next is not None:
        count += 1
        prev = prev.next

    for _ in range(count - n):
        ptr = ptr.next
    ptr.next = ptr.next.next

    return dummy.next