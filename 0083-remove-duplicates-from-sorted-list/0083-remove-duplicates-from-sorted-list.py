# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev=head
        temp=prev.next
        while temp is not None:
            front=temp.next
            if prev.val==temp.val:
                prev.next=front
                temp.next=None
            else:
                prev=temp
            temp=front
        return head

        