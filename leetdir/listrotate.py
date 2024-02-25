from linked_list import ListNode

def listRotate(head, k):
    if not k or not head:
        return head

    last_ptr = head
    count = 1

    while last_ptr.next:
        count += 1
        last_ptr = last_ptr.next


    k %= count

    if k == count:
        return head

    last_ptr.next = head

    ptr_index = count - k - 1

    new_tail = head
    for _ in range(ptr_index):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None


    return new_head




