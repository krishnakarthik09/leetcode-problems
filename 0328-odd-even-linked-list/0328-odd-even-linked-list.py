# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev=head
        temp=prev.next
        even=temp
        while temp is not None and temp.next is not None:
            front=temp.next
            prev.next=front
            temp.next=front.next
            prev=prev.next
            temp=temp.next
        prev.next=even
        return head
        