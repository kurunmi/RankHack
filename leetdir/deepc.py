from linked_list import ListNode
def copyRandom(head):
    old_new = {}
    curr = head

    while curr:
        old_new[curr] = ListNode(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_new[curr.next] = old_new.get(curr.next)
        old_new[curr.random] = old_new.get(curr.random)
        curr = curr.next

    return old_new