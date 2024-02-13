from linked_list import ListNode
def copyRandom(head):
    current = head
    if not head:
        return None

    while current:
        newnode = ListNode(current.val, current.next)
        current = newnode.next

    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    old_head = head
    new_head = head.next
    curr_old = old_head
    curr_new = new_head

    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next

    return new_head





