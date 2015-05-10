# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        ptr = head
        while ptr!= None and ptr.val == val:
            ptr = ptr.next

        if ptr == None or ptr.next == None:
            return ptr

        tmpHead = ptr

        pre = ptr
        ptr = ptr.next
        while ptr != None:
            if ptr.val == val:
                pre.next = ptr.next
                ptr = ptr.next
            else:
                pre = pre.next
                ptr = ptr.next

        return tmpHead

