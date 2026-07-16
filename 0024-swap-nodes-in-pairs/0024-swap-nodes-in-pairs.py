# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev=head
        temp=prev.next
        if temp.next is None:
            temp.next=prev
            prev.next=None
            return temp
        new=head.next
        while temp is not None and temp.next is not None:
            front=temp.next
            temp.next=prev
            if front.next is None:
                prev.next=front
                return new
            else:
                prev.next=front.next
            prev=front
            temp=front.next
        temp.next=prev
        prev.next=None
        return new
        