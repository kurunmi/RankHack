from linked_list import ListNode

def remdupes(head):
    prev = dummy = ListNode(0, head)
    ptr = head

    while ptr and ptr.next:
        if ptr.next.val == ptr.val:
            while ptr.next is not None and ptr.next.val == ptr.val:
                ptr = ptr.next
            ptr.next, ptr = None, ptr.next
            prev = ptr
        else:
            prev = ptr
            ptr = ptr.next

    return dummy.next

