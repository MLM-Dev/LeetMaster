# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		res = 0
		retenu = 0
		ln_one = ListNode()
		ln_while = ln_one

		while l1 or l2 or retenu > 0:
			if retenu > 0:
				ln_while.val = retenu
				retenu = 0
			if l1:
				ln_while.val += l1.val
			if l2:
				ln_while.val += l2.val
			if ln_while.val >= 10:
				ln_while.val = ln_while.val - 10
				retenu = 1
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
			if l1 or l2 or retenu > 0:
				ln_while.next = ListNode()
				ln_while = ln_while.next
		return ln_one