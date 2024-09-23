# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        res = dummy
        curr = head.next
        temp = 0
        while curr:
            if curr.val == 0:
                res.next = ListNode(temp)
                res = res.next
                temp = 0
            else:
                temp += curr.val
            curr = curr.next

        return dummy.next