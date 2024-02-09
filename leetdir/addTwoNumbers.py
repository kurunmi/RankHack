class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(root, item):
    temp = ListNode(item)
    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp

    return root


def display(root):
    while (root != None):
        print(root.val, end=" ")
        root = root.next


def arrayToList(arr):
    n = len(arr)
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
    return root

def addTwoNumbers(l1, l2):
    result = ListNode()
    ptr = result
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        val_sum = val1 + val2 + carry
        carry = val_sum // 10
        val_sum = val_sum % 10
        ptr.next = ListNode(val_sum)
        ptr = ptr.next
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    return result.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1a = [9, 9, 9, 9, 9, 9, 9]
    l2a = [9, 9, 9, 9]
    print(display(addTwoNumbers(arrayToList(l1), arrayToList(l2))))

