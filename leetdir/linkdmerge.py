from linked_list import ListNode
from linked_list import arrayToList
from linked_list import display
from linked_list import insert

def mergelist(list1, list2):
    if not list1:
        return list2
    if not list2:
        return
    iter = newnode = ListNode()
    while list1 is not None and list2 is not None:
        if list1.val >= list2.val:
            iter.next = ListNode(list2.val)
            list2 = list2.next
        else:
            iter.next = ListNode(list1.val)
            list1 = list1.next
        iter = iter.next
    if list1 is not None:
        iter.next = list1
    elif list2 is not None:
        iter.next = list2
    return newnode.next

if __name__ == '__main__':
    list1 = [1, 2, 4]
    list1=arrayToList(list1)
    list2 = [1, 3, 4]
    list2 = arrayToList(list2)
    print(display(mergelist(list1, list2)))

