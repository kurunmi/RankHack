from linked_list import ListNode
from linked_list import arrayToList
from linked_list import display
from linked_list import insert

def mergeTwoLists(list1, list2):
    if not list2:
        return list1
    if not list1:
        return list2
    ptr = result = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            ptr.next = list1
            list1 = list1.next
        else:
            ptr.next = list2
            list2 = list2.next
        ptr = ptr.next
    ptr.next = list1 if list1 else list2
    return result


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(display( mergeTwoLists(arrayToList(list1), arrayToList(list2))))





