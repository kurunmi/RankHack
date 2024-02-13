from linked_list import ListNode
from linked_list import arrayToList
from linked_list import display
def reverseBetween(head, left, right):
    index = head
    n_index = newlist = ListNode()
    y_index = tmp_list = ListNode()
    stack = []
    counter = 0
    while index:
        counter += 1
        print(index.val, counter, left, right)
        while counter < left:
            print('gt')
            n_index = ListNode(index.val)
            n_index = n_index.next
            index = index.next
            counter += 1
            print("head", display(head), display(newlist))
        while left <= counter <= right:
            print('ibw', counter, left, right, index.val)
            stack.append(index.val)
            index = index.next
            print(stack)
            counter += 1
        while counter > right and stack:
            print("stack", stack)
            y_index = ListNode(stack.pop())
            y_index = y_index.next
            print(display(y_index))
        n_index = ListNode(index.val)
        print(index.val)
        n_index = n_index.next
        index = index.next
    return n_index


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    head = arrayToList(head)
    left = 2
    right = 4
    print(display(reverseBetween(head, left, right)))


