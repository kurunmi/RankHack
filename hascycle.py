
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def hasCycle(head):
    slowpointer = head
    fastpointer = head
    while fastpointer and slowpointer.next:
        slowpointer = slowpointer.next
        fastpointer = fastpointer.next.next
        if slowpointer == fastpointer:
            return True

    return False