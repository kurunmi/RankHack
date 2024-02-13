from linked_list import ListNode
from linked_list import arrayToList
from linked_list import display
from linked_list import insert
def cycle1(head):
    pastnodes = set()
    current = head
    while current:
        if current.val in pastnodes:
            return True
        pastnodes.add(current.val)
        current = current.next
    return False

if __name__ == '__main__':
    head = [3,2,0,-4, 2]
    myhead = arrayToList(head)
    display(myhead.next)
    print(cycle1(myhead))