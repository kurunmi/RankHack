def listRotate(head, k):
    if not head or k == 0:
        return head

    count = 1
    ptr = head
    while ptr.next:
        ptr = ptr.next
        count += 1

    k %= count
    k = count - k

    prev = None
    ptr = head

    for _ in range(k):
        prev = ptr
        ptr = ptr.next

    head = ptr
    prev.next = None

    return head

