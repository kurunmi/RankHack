from linked_list import ListNode
from linked_list import arrayToList
from linked_list import display
from linked_list import insert

def twoadd(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    curr = 0
    newlist = ListNode()
    iter = newlist
    while l1 is not None or l2 is not None or curr:
        val1 = l1.val if l1.val is not None else 0
        val2 = l2.val if l2.val is not None else 0
        newval = val1 + val2 + curr
        curr = newval // 10
        newval = newval % 10
        iter.next = ListNode(newval)
        iter = iter.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    return newlist.next

if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = arrayToList(l1)
    l2 = arrayToList(l2)
    print(display(twoadd(l1, l2)))
