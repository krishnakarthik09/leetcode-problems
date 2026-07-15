# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp is not None:
            front =temp.next
            if temp.val==val:
                if temp==head:
                    head=front
                else:
                    prev.next=front
                    temp.next=None
                    temp=None
            if temp is not None:
                prev=temp
            temp=front
        return head
