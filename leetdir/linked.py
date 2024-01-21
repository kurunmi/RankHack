#!/usr/bin/python3





class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Creator:

    def populate(self, in_list):
        # creating the head node
        curr = ListNode(in_list[0])
        head = curr
        # iterating over input list
        for i in in_list[1:]:
            temp = ListNode(i)
            curr.next = temp
            curr = temp

        return head


        # itera
def linked(head):
    slow = head
    fast = head
    while slow is not None:
        print(slow.val)
        slow = slow.next
#    print(slow.val, fast.val, fast.next.val)
#    while slow and fast.next:
#        slow = slow.next
#        fast = fast.next.next
#        print(slow.val, fast.val)
#        if slow == fast:
#            return True
#    return False


if __name__ == '__main__':
    data = [3,2,0,-4]
    node = Creator().populate(data)
    print(linked(node))
