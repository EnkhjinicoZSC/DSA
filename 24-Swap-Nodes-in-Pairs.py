# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nxp = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nxp
            prev.next = second

            prev = curr
            curr = nxp

        return dummy.next

            
