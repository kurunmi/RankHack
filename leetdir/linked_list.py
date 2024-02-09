import math


# Representation of a node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to insert node
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


if __name__=='__main__':
    arr = [1, 2, 3, 4, 5]
    arr1 = [2,4,3]
    root = arrayToList(arr1)
    display(root)