# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	if headA == None or headB == None:
    		return None

    	lenA = self.getListLen(headA)
    	lenB = self.getListLen(headB)

    	ptrLonger = (lenA > lenB) and headA or headB
    	ptrShorter = (lenA > lenB) and headB or headA

    	diffDistance = abs(lenA - lenB)
    	while diffDistance:
    		ptrLonger = ptrLonger.next
    		diffDistance -= 1

    	ptrTarget = None
    	while ptrShorter:
    		if ptrShorter == ptrLonger:
    			ptrTarget = ptrShorter
    			break;
    		ptrShorter = ptrShorter.next
    		ptrLonger = ptrLonger.next
    	return ptrTarget



    def getListLen(self, head):
    	length = 0
    	ptr = head
    	while ptr:
    		length += 1
    		ptr = ptr.next
    	return length
        